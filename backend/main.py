from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.api.poses import analyze_pose

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (mude para o domínio específico em produção)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Pose Analysis API is running!"}

@app.post("/analyze")
async def analyze(file: UploadFile):
    return await analyze_pose(file)
