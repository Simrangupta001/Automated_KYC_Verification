import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=False)

def preprocess_image(img):
    h, w = img.shape[:2]
    img = cv2.resize(img, (w*2, h*2))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.copyMakeBorder(gray, 20,20,20,20, cv2.BORDER_CONSTANT, value=255)

    return gray


def extract_text(crop_img, field_type):

    if field_type == "officer-signature":
        return "[SIGNED]", 1.0

    processed = preprocess_image(crop_img)

    results = reader.readtext(processed)

    texts = []
    confs = []

    for res in results:
        text = res[1].strip()
        conf = res[2]

        if field_type == "citisenship-number":
            text = text.replace(" ", "").replace(".", "")

        texts.append(text)
        confs.append(conf)

    final_text = " ".join(texts)
    avg_conf = sum(confs)/len(confs) if confs else 0

    return final_text, avg_conf