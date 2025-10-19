# API de One Piece - FastAPI + MongoDB

## Descripción
API REST para gestionar personajes del mundo de One Piece. Permite crear, listar y eliminar personajes, además de realizar búsquedas personalizadas por tripulación, recompensa y usuarios de frutas del diablo.

## Características

- ✅ **Listar todos los personajes** - Obtén la lista completa de nakamas
- ✅ **Crear nuevos personajes** - Añade piratas, marines y más
- ✅ **Eliminar personajes** - Gestiona tu tripulación
- ✅ **Buscar por tripulación** - Encuentra miembros de tripulaciones específicas
- ✅ **Top recompensas** - Descubre quiénes son los más buscados
- ✅ **Usuarios de frutas del diablo** - Filtra por habilidades especiales

## Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y rápido
- **MongoDB** - Base de datos NoSQL
- **Python 3.x** - Lenguaje de programación
- **Pymongo** - Driver de MongoDB para Python
- **Uvicorn** - Servidor ASGI

## Modelo de Datos

Cada personaje contiene:
- `nombre`: Nombre del personaje
- `recompensa`: Recompensa en berries (número)
- `fruta_diablo`: Nombre de la fruta del diablo (opcional)
- `tripulacion`: Nombre de la tripulación
- `rol`: Rol en la tripulación

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/api-onepiece.git
cd api-onepiece
```

### 2. Crear entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
MONGODB_URL=tu_url_de_mongodb
DB_NAME=onepiece_db
```

### 5. Ejecutar la aplicación
```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

## 📚 Documentación de Endpoints

### Documentación interactiva
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Endpoints disponibles

#### CRUD Básico

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/personajes` | Lista todos los personajes |
| POST | `/personajes` | Crea un nuevo personaje |
| DELETE | `/personajes/{id}` | Elimina un personaje |

#### Búsquedas Especializadas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/personajes/tripulacion/{tripulacion}` | Busca por tripulación |
| GET | `/personajes/recompensa/top` | Top personajes por recompensa |
| GET | `/personajes/fruta-diablo` | Usuarios de frutas del diablo |

## 💡 Ejemplos de Uso

### Crear un personaje
```bash
curl -X POST "http://127.0.0.1:8000/personajes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Monkey D. Luffy",
    "recompensa": 3000000000,
    "fruta_diablo": "Gomu Gomu no Mi",
    "tripulacion": "Piratas del Sombrero de Paja",
    "rol": "Capitán"
  }'
```

### Listar todos los personajes
```bash
curl -X GET "http://127.0.0.1:8000/personajes"
```

### Buscar por tripulación
```bash
curl -X GET "http://127.0.0.1:8000/personajes/tripulacion/Sombrero"
```

## 📸 Capturas de Pantalla

### Interfaz Swagger
*[Aquí se incluyen las capturas de Swagger UI mostrando los endpoints]*

### Operaciones CRUD
*[Capturas de las operaciones de alta, listado y baja]*

### Base de Datos MongoDB
*[Capturas de MongoDB Compass mostrando los documentos]*

## 📁 Estructura del Proyecto

```
api-onepiece/
│
├── main.py              # Archivo principal con los endpoints
├── models.py            # Modelos Pydantic
├── database.py          # Configuración de MongoDB
├── .env                 # Variables de entorno (no incluido en Git)
├── .gitignore          # Archivos ignorados
├── requirements.txt     # Dependencias
├── README.md           # Este archivo
└── screenshots/        # Capturas de pantalla
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 👨‍💻 Autor

[Antonio Lorenzo Cano Jiménez]

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🙏 Agradecimientos

- Eiichiro Oda por crear One Piece
- FastAPI por su excelente framework
- MongoDB por su poderosa base de datos

---

⚓ *"¡Voy a ser el Rey de los Piratas!"* - Monkey D. Luffy
