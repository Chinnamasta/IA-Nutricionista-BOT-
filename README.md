**🤖 Bot Nutricionista com IA no Telegram:**
Este projeto visa desenvolver um agente conversacional de inteligência artificial que atua como um nutricionista virtual no Telegram. Através deste bot, os usuários podem interagir de forma natural e personalizada, recebendo orientações nutricionais e suporte em saúde e bem-estar. O projeto integra processamento de linguagem natural e análise de imagens para criar uma experiência completa de monitoramento e aconselhamento nutricional.

**✨ Funcionalidades Principais:**
- Interação Conversacional: Converse com a IA Nutricionista no Telegram de forma natural e intuitiva.
- Análise de Refeições por Imagem: Envie fotos de seus pratos de comida para receber análises e tabelas nutricionais.
- Orientação Nutricional Personalizada: Receba suporte e orientações de saúde e bem-estar.
- Gerenciamento de Contexto: O bot mantém o contexto das conversas para interações mais fluidas e relevantes.
- Ferramentas Personalizadas: O agente utiliza ferramentas customizadas para ampliar suas capacidades de resposta e análise.
- Registro de Informações: Capacidade de registrar informações nutricionais.
- Geração de Planos de Dieta: Potencial para gerar planos de dieta personalizados (depende da implementação completa do agente).

**🚀 Tecnologias e Bibliotecas Utilizadas:**
- Python: Linguagem de programação principal.
- LangChain: Framework para desenvolvimento de agentes conversacionais baseados em LLMs.
- OpenAI API: Integração com modelos de linguagem avançados para processamento de linguagem natural e geração de respostas.
- TinyDB: Banco de dados NoSQL leve para gerenciamento e persistência de dados.
- Pyrogram: Biblioteca para criação de bots Telegram.
- Python-dotenv: Para gerenciamento de variáveis de ambiente.
- Logging: Para registro de eventos e depuração.
- Asyncio: Para programação assíncrona.

**🛠️ Configuração e Instalação (WIP):**
Para configurar e rodar o projeto localmente, siga os passos abaixo:
- Clone o repositório:
git clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git
cd NomeDoSeuRepositorio
- Crie um ambiente virtual com Poetry:
Se você ainda não tem Poetry instalado, siga as instruções em Poetry Installation.
poetry install
- Ative o ambiente virtual (se ainda não estiver ativado):
poetry shell
- Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto com suas credenciais do Telegram e OpenAI:
TELEGRAM_API_ID=SEU_API_ID_DO_TELEGRAM
TELEGRAM_API_HASH=SEU_API_HASH_DO_TELEGRAM
TELEGRAM_BOT_TOKEN=SEU_BOT_TOKEN_DO_TELEGRAM
OPENAI_API_KEY=SUA_CHAVE_API_DA_OPENAI
- Obtenha seu API ID e API Hash em my.telegram.org.
- Obtenha seu Bot Token conversando com o @BotFather no Telegram.
- Obtenha sua OpenAI API Key em platform.openai.com.
- Estrutura de Pastas e __init__.py:
Certifique-se de que os arquivos __init__.py existam em todos os diretórios que contêm módulos Python para que as importações funcionem corretamente. A estrutura deve ser similar a:
.
├── __init__.py
├── app.py
├── .env
├── agents/
│   ├── __init__.py
│   └── nutritionist.py
├── chat/
│   ├── __init__.py
│   └── telegram.py
└── repositories/
    ├── __init__.py
    └── meal_entry.py
# ... outros arquivos e diretórios

- Executar o Bot:
Com o ambiente virtual ativado e as variáveis de ambiente configuradas, execute o script principal:
python app.py

**🤝 Contribuição:**
- Este projeto está em desenvolvimento contínuo e a colaboração é muito bem-vinda! Se você deseja contribuir, sinta-se à vontade para:
- Fazer um fork do repositório.
- Criar uma branch para sua feature (git checkout -b feature/minha-feature).
- Fazer suas alterações e commit (git commit -m 'feat: adiciona nova funcionalidade').
- Fazer push para a branch (git push origin feature/minha-feature).
- Abrir um Pull Request.
- Toda contribuição é valorizada!
