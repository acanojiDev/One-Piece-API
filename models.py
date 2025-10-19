from pydantic import BaseModel, Field
from typing import Optional

class Personaje(BaseModel):
	nombre: str
	recompensa: int = Field(..., description="Recompensa en berries")
	fruta_diablo: Optional[str] = Field(None, description="Nombre de la fruta del diablo")
	tripulacion: str
	rol: str
	img:Optional[str] = Field(None, description="Imagen del personaje")
	
	class Config:
		json_schema_extra = {
			"example": {
				"nombre": "Monkey D. Luffy",
				"recompensa": 30000000,
				"fruta_diablo": "Gomu Gomu no Mi (Hito Hito no mi, Modelo: Nika)",
				"tripulacion": "Piratas del Sombrero de Paja",
				"rol": "Capitán",
				"img": "https://static.wikia.nocookie.net/onepiece/images/6/6d/Monkey_D._Luffy_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20240306200817"
			}
		}

class PersonajeResponse(Personaje):
	id: str
