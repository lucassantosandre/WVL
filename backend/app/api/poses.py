import mediapipe as mp
import cv2
import math
from fastapi import UploadFile
from fastapi.responses import JSONResponse
import os

# Inicializa MediaPipe Pose e Desenho
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Função para calcular ângulo entre três pontos
def calculate_angle(a, b, c):
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

    feedback = "Pose analyzed successfully"
    angles = {}
    annotated_image_path = None

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

        # Salva a imagem anotada no diretório acessível
        output_dir = "./annotated_images"
        os.makedirs(output_dir, exist_ok=True)  # Cria o diretório, se necessário
        annotated_image_path = f"{output_dir}/annotated_{file.filename}"
        cv2.imwrite(annotated_image_path, annotated_image)

        # Limpa o arquivo temporário original
        os.remove(file_location)

    else:
        feedback = "No pose landmarks detected"
        os.remove(file_location)  # Remove o arquivo original

    # Resposta JSON com a URL da imagem e ângulos calculados
    response = {
        "image_url": f"/annotated_images/annotated_{file.filename}" if annotated_image_path else None,
        "angles": angles,
        "message": feedback,
    }
    return JSONResponse(content=response)
