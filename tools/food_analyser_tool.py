from io import BytesIO
import base64
from langchain.tools import BaseTool
from PIL import image
from langchain_openai import ChatOpenAI
from langchain_core.message import HumanMessage


class FoodImageAnalyserTool(BaseTool):
    name: str = "food_image_analyser"
    description: str = '''
            Utilize esta ferramenta para analisar imagens de pratos de comida que usuário enviar. Descreva os alimentos presentes e crie uma tabela nutricional da refeição.
            O agente deve usar esta ferramenta sempre que um caminho de imagem for fornecido, mas somente quando o input for um caminho de imagem.
'''

    def run(self, image_path: str) -> str:
        image = Image.open(image_path)
        buffered = BytesIO
        image.save = (buffered, format = 'JPEG')
        img_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            

        instructions = """
        Você deve analisar a imagem enviada e verificar se ela contém um prato de comida.
        Caso seja prato de comida, descreva os itens visíveis no prato e crie uma descrição nutricional detalhada e estimada
        incluindo calorias, carboidratos, proteínas e gorduras. Forneça uma descrição nutricional completa da refeição.
        """


        llm = ChatOpenAI(
            model = "gpt-4o-mini"
        )
        message = [HumanMessage(
            content = [
                {'type': 'text', 'text': instructions},
                {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{img_b64}'}}
            ]
        )]

        response = llm.invoke(message)
        return response

    async def _arun(self, image_path: str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
