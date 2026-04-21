from ultralytics import YOLO
import cv2
import os

class CitizenshipDetector:

    def __init__(self, model_path: str):
        self.model = YOLO(model_path)
        self.min_conf = 0.2

    def detect_and_crop(self, image_path: str, output_dir: str):
        img = cv2.imread(image_path)

        if img is None:
            raise ValueError("Image not found")

        os.makedirs(output_dir, exist_ok=True)

        results = self.model(img, conf=self.min_conf)

        detections = []

        for i, box in enumerate(results[0].boxes):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            label = self.model.names[cls_id]

            crop = img[y1:y2, x1:x2]

            crop_path = os.path.join(output_dir, f"{label}_{i}.jpg")
            cv2.imwrite(crop_path, crop)

            detections.append({
                "class_name": label,
                "confidence": conf,
                "crop_path": crop_path
            })

        return detections

    def detect_back(self, image_path, output_dir):
        return self.detect_and_crop(image_path, output_dir)