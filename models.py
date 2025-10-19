from pydantic import BaseModel, Field
from typing import Optional

class Personaje(BaseModel):
	nombre: str
	recompensa: int = Field(..., description="Recompensa en berries")
	fruta_diablo: Optional[str] = Field(None, description="Nombre de la fruta del diablo")
	tripulacion: str
	rol: str

	class Config:
		json_schema_extra = {
			"example": {
				"nombre": "Monkey D. Luffy",
				"recompensa": 30000000,
				"fruta_diablo": "Gomu Gomu no Mi (Hito Hito no mi, Modelo: Nika)",
				"tripulacion": "Piratas del Sombrero de Paja",
				"rol": "Capitán"
			}
		}

class PersonajeResponse(Personaje):
	id: str
