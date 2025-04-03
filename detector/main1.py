from users import User
from tasks import PredictionTask
from models import MLModel
from results import PredictionResult
import json

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
    input_data=json.dumps({"image": "images/construction_site.jpg"}),
    ml_model=hard_hat_model
)

# Запускаем задачу
result = safety_check_task.run()

# Проверяем результаты
if result.get_violation_type() == "No Hard Hat":
    print("Violation detected! No hard hat found.")
else:
    print("No violations detected.")