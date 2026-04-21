import re

class KycCleaner:

    def clean(self, field, text, conf=1.0):

        if field != "citisenship-number":
            return text

        if not text:
            return ""

        text = text.upper()

        text = (
            text.replace("O", "0")
                .replace("I", "1")
                .replace("L", "1")
                .replace("S", "5")
        )

        cleaned = re.sub(r'[^0-9]', '', text)

        return cleaned if len(cleaned) >= 10 else ""