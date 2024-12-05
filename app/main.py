from fastapi import FastAPI
from app.schemas import WorkoutRequest, WorkoutResponse
from app.services import calculate_volume_and_intensity

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Simulador de Volume de Treino"}

@app.post("/calculate", response_model=WorkoutResponse)
def calculate_workout(data: WorkoutRequest):
    result = calculate_volume_and_intensity(data)
    return result
