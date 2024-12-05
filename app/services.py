from app.schemas import WorkoutRequest

def calculate_volume_and_intensity(data: WorkoutRequest):
    total_volume = 0
    exercise_volumes = {}
    work_volume = 0  # Volume das séries de trabalho (alta intensidade)
    warmup_volume = 0  # Volume das séries de aquecimento

    for exercise in data.exercises:
        exercise_volume = 0
        for idx, set_data in enumerate(exercise.sets):
            set_volume = set_data.reps * set_data.weight
            exercise_volume += set_volume

            # Diferenciar aquecimento e trabalho
            if idx < 2:  # As 2 primeiras séries são de aquecimento
                warmup_volume += set_volume
            else:  # As 2 últimas séries são de trabalho
                work_volume += set_volume

        exercise_volumes[exercise.exercise_name] = exercise_volume
        total_volume += exercise_volume

    # Ajustar as sugestões para alta intensidade
    if work_volume > 0.8 * total_volume:
        suggestions = "O treino está adequado para alta intensidade. Certifique-se de estar recuperando bem entre sessões."
    else:
        suggestions = (
            "Considere reduzir o volume de aquecimento ou ajustar as séries de trabalho "
            "para aumentar a intensidade."
        )

    return {
        "exercise_volumes": exercise_volumes,
        "total_volume": total_volume,
        "warmup_volume": warmup_volume,
        "work_volume": work_volume,
        "suggestions": suggestions,
        "progression_details": {}  # Adicione um dicionário vazio ou com detalhes apropriados
    }