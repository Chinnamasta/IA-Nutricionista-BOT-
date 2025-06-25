from pydantic import BaseModel, Field

class User(BaseModel):
    telegram_id: int = Field(..., description = 'O ID do usuário do Telegram.')
    nome: str = Field(..., description = 'O nome completo do usuário.')
    sex: str = Field(..., description = 'O sexo do usuário. Exemplo: 'M' para Masculino e 'F' para Feminino.')
    age: str = Field(..., description = 'A idade do usuário. Exemplo: '25 anos'.')
    height_cm: str = Field(..., description = 'A altura do usuário em cm. Exemplo: '180 cm' .')
    weight_kg: str = Field(..., description = 'O peso do usuário em quilogramas. Exemplo: '70 kilos'.')
    has_diabetes: str = Field(..., description = 'Indica se o usuário tem diabetes. Exemplo: 'Sim' ou 'Não'.')
    goal: str = Field(..., description = 'O objetivo do usuário com IA Nutricionista. Exemplo: 'Perder peso', 'Ganhar peso', 'Ganhar massa muscular'.')
    
