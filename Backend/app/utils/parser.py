import cv2
from .ocr import extract_text
from .cleaner import KycCleaner

CLASS_NAME_MAP = {
    "citisenship-number": "citisenship-number"
}

MIN_CONF = 0.5


def parse_fields(detections):

    cleaner = KycCleaner()

    for det in detections:
        if det["class_name"] != "citisenship-number":
            continue

        if det["confidence"] < MIN_CONF:
            continue

        img = cv2.imread(det["crop_path"])

        raw, _ = extract_text(img, "citisenship-number")

        cleaned = cleaner.clean("citisenship-number", raw)

        return cleaned

    return ""