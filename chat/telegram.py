import logging
import asyncio
import os
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
# Certifique-se de que 'projeto/agents/__init__.py' existe para esta importação funcionar.
# A raiz do seu projeto (C:\Users\Padma\Desktop\projeto) também precisa de um __init__.py
from projeto.agents.nutritionist import NutritionistAgent
from pyrogram.enums import ChatAction
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env.
# Certifique-se de que o arquivo .env esteja na raiz do seu projeto (C:\Users\Padma\Desktop\projeto\)
load_dotenv()

class TelegramBot:
    def __init__(self):
        # Configuração básica de log para exibir informações no console
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
        
        # Inicialização do cliente Pyrogram
        # Verifique se 'TELEGRAM_API_ID', 'TELEGRAM_API_HASH' e 'TELEGRAM_BOT_TOKEN'
        # estão definidos no seu arquivo .env
        self.app = Client(
            name='Agente_Nutricionista_bot',
            api_id = os.getenv('TELEGRAM_API_ID'),
            api_hash=os.getenv('TELEGRAM_API_HASH'),
            # Usar TELEGRAM_BOT_TOKEN para consistência com as boas práticas
            bot_token=os.getenv('TELEGRAM_BOT_TOKEN') 
        )

        # Verificação das variáveis de ambiente
        if not self.app.api_id or not self.app.api_hash or not self.app.bot_token:
            self.logger.critical("Erro: Variáveis de ambiente TELEGRAM_API_ID, TELEGRAM_API_HASH ou TELEGRAM_BOT_TOKEN não estão definidas.")
            # É importante que o bot não tente rodar sem as credenciais
            raise ValueError("As credenciais do bot Telegram não estão configuradas corretamente.")


        self._setup_handlers() # Configura os manipuladores de mensagens e fotos

    def _setup_handlers(self):
        # Handler para o comando /start
        start_handler = MessageHandler(
            self.start,
            filters.command("start") & filters.private # Responde apenas a comandos /start em chats privados
        )
        self.app.add_handler(start_handler)

        # Handler para mensagens de texto
        text_filter = filters.text & filters.private # Responde apenas a mensagens de texto em chats privados
        message_handler = MessageHandler(
            self.handle_message,
            text_filter
        )
        self.app.add_handler(message_handler)

        # Handler para fotos
        photo_filter = filters.photo & filters.private # Responde apenas a fotos em chats privados
        photo_handler = MessageHandler(
            self.handle_photo,
            photo_filter
        )
        self.app.add_handler(photo_handler)

    async def start(self, client: Client, message: Message):
        # Envia uma mensagem de boas-vindas quando o usuário inicia o bot
        await message.reply_text(
            'Olá! Eu sou sua IA Nutricionista. Envie uma mensagem ou foto de um prato de comida para começar.'
        )
        self.logger.info(f"Usuário {message.from_user.id} iniciou uma conversa.")

    async def handle_message(self, client: Client, message: Message):
        user_id = message.from_user.id
        user_input = message.text

        # Envia uma ação de "digitando" para o usuário
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

        # Instancia o Agente Nutricionista com o ID da sessão do usuário
        agent = NutritionistAgent(session_id=str(user_id))

        try:
            # Executa o agente com a mensagem de texto do usuário
            # O formato da entrada 'telegram_id: {user_id} mensagem: {user_input}' deve ser processado pelo agente
            response = agent.run(f'telegram_id: {user_id} mensagem: {user_input}')
        except Exception as err:
            self.logger.error(f"Erro ao processar a mensagem do usuário {user_id}: {err}", exc_info=True)
            response = "Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."

        # Envia a resposta do agente de volta ao usuário
        await message.reply_text(response)
        self.logger.info(f"Resposta enviada para o usuário {user_id}.")

    async def handle_photo(self, client: Client, message: Message):
        user_id = message.from_user.id

        # Envia uma ação de "digitando" para o usuário
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

        # Cria o diretório 'storage' se ele não existir
        storage_dir = os.path.join(os.getcwd(), 'storage')
        os.makedirs(storage_dir, exist_ok=True)

        # Define o nome e o caminho do arquivo da foto
        photo_file_name = f"{user_id}_{message.photo.file_id}.jpg"
        photo_path = os.path.join(storage_dir, photo_file_name)
        
        # Faz o download da foto
        await message.download(file_name=photo_path)

        # Instancia o Agente Nutricionista com o ID da sessão do usuário
        agent = NutritionistAgent(session_id=str(user_id))

        try:
            # Executa o agente com o caminho da foto
            response = agent.run(photo_path)
        except Exception as err:
            self.logger.error(f"Erro ao processar a foto do usuário {user_id}: {err}", exc_info=True)
            response = "Desculpe, ocorreu um erro ao processar sua imagem. Por favor, tente novamente."
        finally:
            # Opcional: Remover a foto após o processamento para economizar espaço
            if os.path.exists(photo_path):
                os.remove(photo_path)
                self.logger.info(f"Foto {photo_path} removida após o processamento.")


        # Envia a resposta do agente de volta ao usuário
        await message.reply_text(response)
        self.logger.info(f"Resposta enviada para o usuário {user_id}.")

    def run(self):
        self.logger.info("Bot Telegram iniciado.")
        # Inicia o cliente Pyrogram e mantém-o rodando
        self.app.run()
