from typing import Any
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class PredictionResult:
    def __init__(self, task_id: int, result: Any, violation_type: str, response_status: str):
        self.task_id = task_id
        self.result = result
<<<<<<< Updated upstream
        self.violation_type = violation_type  # Добавлен новый параметр
        self.response_status = response_status  # Добавлен новый параметр

    def get_violation_type(self) -> str:
        return self.violation_type  # Новый геттер для типа нарушения

    def get_response_status(self) -> str:
        return self.response_status  # Новый геттер для статуса реакции
=======
        self.violation_type = violation_type
        self.response_status = response_status

    def get_violation_type(self) -> str:
        return self.violation_type

    def get_response_status(self) -> str:
        return self.response_status
>>>>>>> Stashed changes
