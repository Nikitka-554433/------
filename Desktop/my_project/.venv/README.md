# Используется модель YOLOv8n для детектирования строительных касок
# Источник: keremberke/yolov8n-hard-hat-detection
## Проект: Контроль Безопасности Труда

## Цель проекта
## Автоматическая система для мониторинга соблюдения норм охраны труда на строительных объектах с использованием машинного обучения.

## Используемые технологии
- **Машинное обучение**: YOLOv8n (детектор строительных касок)
- **Библиотеки**: ultralyticsplus, OpenCV, NumPy

from ultralyticsplus import YOLO, render_result

# load model
model = YOLO('keremberke/yolov8n-hard-hat-detection')

# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

# set image
image = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model.predict(image)

# observe results
print(results[0].boxes)
render = render_result(model=model, image=image, result=results[0])
render.show()
