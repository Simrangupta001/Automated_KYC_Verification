from app.utils.detector import CitizenshipDetector
from app.utils.parser import parse_fields

MODEL_PATH = "ml/docservice/weights/best.pt"

detector = CitizenshipDetector(MODEL_PATH)


def verify_citizenship(image_path, user_input_number):

    detections = detector.detect_back(image_path, "ml/docservice/crops")

    extracted_number = parse_fields(detections)

    if not extracted_number:
        return {"status": "fail", "message": "No number detected"}

    if extracted_number == user_input_number:
        return {"status": "success", "message": "Verified"}

    return {
        "status": "fail",
        "message": "Number mismatch",
        "extracted": extracted_number
    }