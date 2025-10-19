from fastapi import FastAPI, HTTPException, status
from models import Personaje, PersonajeResponse
from database import personajes_collection
from bson import ObjectId
from typing import List

app = FastAPI(
	title = "API de One Piece",
	description = "API para gestionar personajes del mundo de One Piece",
	version="1.0.0"
)

def personaje_helper(personaje)-> dict:
	"""Convierte un documento de MongoDB a diccionario"""
	return {
		"id": str(personaje["_id"]),
		"nombre": personaje["nombre"],
		"recompensa": personaje["recompensa"],
		"fruta_diablo": personaje.get("fruta_diablo"),
		"tripulacion": personaje["tripulacion"],
		"rol":personaje["rol"]
	}

@app.get("/", tags=["Root"])
async def root():
	"""Endpoint raíz"""
	return {
		"mensaje": "¡Bienvenido a la API de One Piece!",
		"navegando_hacia": "El One Piece"
	}

@app.get("/personajes", response_model=List[PersonajeResponse], tags=["Personajes"])
async def listar_personajes():
	"""Obtiene la lista completa de personajes"""
	personajes = []
	for personaje in personajes_collection.find():
		personajes.append(personaje_helper(personaje))
	return personajes

@app.post("/personajes", response_model=PersonajeResponse, status_code=status.HTTP_201_CREATED, tags=["Personajes"])
async def crear_personaje(personaje: Personaje):
	"""Crea un nuevo personaje"""
	personaje_dict = personaje.model_dump()
	resultado = personajes_collection.insert_one(personaje_dict)

	nuevo_personaje = personajes_collection.find_one({"_id": resultado.inserted_id})
	return personaje_helper(nuevo_personaje)

@app.delete("/personajes/{personaje_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Personajes"])
async def eliminar_personaje(personaje_id: str):
    """Elimina un personaje por su ID"""
    try:
        resultado = personajes_collection.delete_one({"_id": ObjectId(personaje_id)})

        if resultado.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Personaje con id {personaje_id} no encontrado"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )

@app.get("/personajes/recompensa/top", response_model=List[PersonajeResponse], tags=["Búsquedas"])
async def top_recompensas(limit: int = 5):
    """Obtiene los personajes con mayor recompensa"""
    personajes = []
    for personaje in personajes_collection.find().sort("recompensa", -1).limit(limit):
        personajes.append(personaje_helper(personaje))
    return personajes

@app.get("/personajes/fruta-diablo", response_model=List[PersonajeResponse], tags=["Búsquedas"])
async def con_fruta_diablo():
    """Obtiene personajes que tienen fruta del diablo"""
    personajes = []
    for personaje in personajes_collection.find({"fruta_diablo": {"$ne": None}}):
        personajes.append(personaje_helper(personaje))
    return personajes

