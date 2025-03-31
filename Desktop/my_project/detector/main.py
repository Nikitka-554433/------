from typing import Any

class User:
    def __init__(self, id: int, username: str, email: str, password_hash: str, role: str):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role

class MLModel:
    def __init__(self, name: str, overrides: dict):
        self.name = name
        self.overrides = overrides

    def set_overrides(self, conf: float, iou: float, agnostic_nms: bool, max_det: int):
        self.overrides['conf'] = conf
        self.overrides['iou'] = iou
        self.overrides['agnostic_nms'] = agnostic_nms
        self.overrides['max_det'] = max_det

    def predict(self, input_data: Any) -> Any:
        # Здесь выполняется предикт с использованием заданной модели
        # Возвращается результат предсказания
        return input_data  # Пример возврата входных данных

class PredictionResult:
    def __init__(self, task_id: int, result: Any, violation_type: str, response_status: str):
        self.task_id = task_id
        self.result = result
        self.violation_type = violation_type
        self.response_status = response_status

    def get_violation_type(self) -> str:
        return self.violation_type

class PredictionTask:
    def __init__(self, id: int, description: str, input_data: Any, ml_model: MLModel):
        self.id = id
        self.description = description
        self.input_data = input_data
        self.ml_model = ml_model

    def run(self) -> PredictionResult:
        # Выполняем предсказание с использованием модели
        result = self.ml_model.predict(self.input_data)
        return PredictionResult(self.id, result, "No Hard Hat", "Not Handled")  # Допустим, здесь фиксировано "No Hard Hat"

# Создаем экземпляр класса MLModel
hard_hat_model = MLModel(name="Hard Hat Detection Model", overrides={})

# Создаем пользователя-инспектора
inspector = User(id=1, username="Inspector", email="inspector@example.com", password_hash="hashed_password", role="inspector")

# Настраиваем параметры модели
hard_hat_model.set_overrides(conf=0.25, iou=0.45, agnostic_nms=False, max_det=1000)

# Создаем задачу на проверку изображений рабочего места
safety_check_task = PredictionTask(
    id=1,
    description="Check for hard hat violations",
    input_data="images/construction_site.jpg",
    ml_model=hard_hat_model
)

# Запускаем задачу
result = safety_check_task.run()

# Проверяем результаты
if result.get_violation_type() == "No Hard Hat":
    print("Violation detected! No hard hat found.")
else:
    print("No violations detected.")