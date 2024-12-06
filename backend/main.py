from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.poses import analyze_pose

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta o diretório de imagens como estático
app.mount("/annotated_images", StaticFiles(directory="annotated_images"), name="annotated_images")

@app.post("/analyze")
async def analyze(file: UploadFile):
    return await analyze_pose(file)

@app.get("/")
def root():
    return {"message": "Pose Analysis API is running!"}
