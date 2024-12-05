import mediapipe as mp
import cv2
import math
from fastapi import UploadFile
from fastapi.responses import FileResponse
import os

# Inicializa MediaPipe Pose e Desenho
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Função para calcular ângulo entre três pontos
def calculate_angle(a, b, c):
    """
    Calcula o ângulo entre três pontos:
    a: Primeiro ponto (x, y, z)
    b: Ponto central (x, y, z)
    c: Terceiro ponto (x, y, z)
    """
    ang = math.degrees(
        math.atan2(c[1] - b[1], c[0] - b[0]) -
        math.atan2(a[1] - b[1], a[0] - b[0])
    )
    return abs(ang)

# Função para processar a pose
async def analyze_pose(file: UploadFile):
    # Salva o arquivo temporariamente
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Carrega a imagem
    img = cv2.imread(file_location)

    # Inicializa o MediaPipe Pose
    pose = mp_pose.Pose(static_image_mode=True)
    results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Feedback inicial
    feedback = "Pose analyzed successfully"
    angles = {}

    # Verifica se landmarks foram detectados
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Extrai coordenadas dos landmarks relevantes
        def get_coords(index):
            return (landmarks[index].x, landmarks[index].y, landmarks[index].z)

        # Cálculo de ângulos (exemplo com cotovelo direito)
        try:
            right_elbow_angle = calculate_angle(
                get_coords(11),  # Ombro direito
                get_coords(13),  # Cotovelo direito
                get_coords(15)   # Pulso direito
            )
            angles["right_elbow"] = right_elbow_angle

            # Feedback baseado no ângulo
            if right_elbow_angle < 80 or right_elbow_angle > 100:
                feedback += " | Adjust your right elbow to approximately 90 degrees."
        except IndexError:
            feedback += " | Could not calculate right elbow angle."

        # Sobreposição de landmarks na imagem
        annotated_image = img.copy()
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        # Salva a imagem anotada
        output_path = f"annotated_{file.filename}"
        cv2.imwrite(output_path, annotated_image)

        # Limpa o arquivo temporário original
        os.remove(file_location)

        # Retorna a imagem anotada junto com os ângulos calculados
        return {
            "image": FileResponse(output_path, media_type="image/jpeg", filename=f"annotated_{file.filename}"),
            "angles": angles,
            "message": feedback
        }

    # Caso nenhum landmark seja detectado
    feedback = "No pose landmarks detected"
    os.remove(file_location)  # Remove o arquivo original mesmo se falhar
    return {"message": feedback, "angles": angles}
