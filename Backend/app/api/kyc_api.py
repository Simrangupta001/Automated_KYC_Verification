from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
import uuid
from app.services.kyc_service import verify_citizenship

router = APIRouter()

UPLOAD_DIR = "ml/docservice/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/verify-kyc")
async def verify_kyc(
    file: UploadFile = File(...),
    citizenship_number: str = Form(...)
):

    try:
        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = verify_citizenship(file_path, citizenship_number)

        return result

    except Exception as e:
        return {"error": str(e)}