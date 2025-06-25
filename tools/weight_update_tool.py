from langchain.tools import BaseTool
from projeto.repositories.user import UserRepository
from projeto.repositories.weight_history import WeightHistoryRepository


class WeightUpdateTool(BaseTool):
    name: str = "weight_update"
    description: str = (
        "Use essa ferramenta para registrar o peso de um usuário."
        "Entrada: telegram_id do usuário e weight_id."
    )

    def __init__(self):
        super().__init__()
        self._user_repo = UserRepository()
        self._weight_history_repo = WeightHistoryRepository()

    def _run(self, telegram_id: int, weight_kg: str) -> str:
        try:
            user = self._user_repo.get_user_by_telegram_id(telegram_id)
            if not user:
                return f"Usuário não encontrado. Por favor, registre-se primeiro."
            
            self._weight_history_repo.add_weight_entry(telegram_id, weight_kg)
            return f"Peso atualizado com sucesso para {user.name}."
        except Exception as err:
            return f"Erro na ferramenta de atualização de peso: {str(err)}"


    async def _arun(self, weight_kg: float) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
