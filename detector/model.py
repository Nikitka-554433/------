from typing import Any

class MLModel:
    def __init__(self, name: str, overrides: dict):
        self.name = name
        self.overrides = overrides

<<<<<<< Updated upstream
    def predict(self, input_data: Any) -> Any:
        # Здесь выполняется предикт с использованием заданной модели
        # Возвращается результат предсказания
        return input_data  # Пример возврата входных данных

# Создаем экземпляр класса MLModel
hard_hat_model = MLModel(name="Hard Hat Detection Model", overrides={})

class PredictionResult:
    def __init__(self, task_id: int, result: Any):
        self.task_id = task_id
        self.result = result

class PredictionTask:
    def __init__(self, id: int, description: str, input_data: Any, ml_model: MLModel):
        self.id = id
        self.description = description
        self.input_data = input_data
        self.ml_model = ml_model

    def run(self) -> PredictionResult:
        # Выполняем предсказание с использованием модели
        result = self.ml_model.predict(self.input_data)
        return PredictionResult(self.id, result)
=======
    def set_overrides(self, conf: float, iou: float, agnostic_nms: bool, max_det: int):
        self.overrides['conf'] = conf
        self.overrides['iou'] = iou
        self.overrides['agnostic_nms'] = agnostic_nms
        self.overrides['max_det'] = max_det

    def predict(self, input_data: Any) -> Any:
        
        return input_data  # Пример возврата входных данных
>>>>>>> Stashed changes
