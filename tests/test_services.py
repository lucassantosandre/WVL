from app.services import calculate_volume_and_intensity
from app.schemas import ExerciseData

def test_calculate_volume_and_intensity():
    data = ExerciseData(exercise_name="Agachamento", weight=100, reps=10, sets=4)
    result = calculate_volume_and_intensity(data)

    assert result["total_volume"] == 4000
    assert 60 <= result["average_intensity"] <= 70
    assert "hipertrofia" in result["suggestions"]
