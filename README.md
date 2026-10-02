# 🇳🇵 Automated KYC Verification System (Nepali Citizenship)

An AI-powered **eKYC (Electronic Know Your Customer)** system designed to automate the verification of **Nepali Citizenship Cards** using Computer Vision and OCR.


---

## 🚀 Overview

This project aims to simplify and automate the KYC verification process by extracting and validating information from citizenship documents.

Users can upload an image of a citizenship card and provide their citizenship number. The system processes the image using AI models and verifies the provided information.

---

## ✨ Current Features

- 📄 Upload citizenship image (JPG/PNG)
- 🔍 Detect key regions using YOLO (Object Detection)
- 🧠 Extract text using OCR (EasyOCR)
- 🧹 Basic text cleaning and parsing
- ✅ Citizenship number verification
- 🌐 Simple React-based frontend UI
- ⚡ FastAPI backend for API handling

---

## ⚙️ Tech Stack

### 🔹 Backend
- FastAPI
- Python
- Ultralytics YOLOv8
- EasyOCR
- OpenCV

### 🔹 Frontend
- React.js
- Tailwind CSS

### 🔹 Machine Learning
- YOLOv8 (custom trained model)
- OCR pipeline for text extraction

---  project/
│
├── Backend/
│ ├── app/
│ │ ├── api/ # API routes
│ │ ├── services/ # Business logic
│ │ ├── utils/ # Detection + OCR utilities
│ │ └── main.py # FastAPI entry point
│
├── ml/
│ ├── docservice/
│ │ ├── weights/ # YOLO model (best.pt)
│ │ ├── uploads/ # Uploaded files
│
├── frontend/
│ └── src/
│ └── App.js # React UI


---

## 🔄 How It Works

1. User uploads a citizenship image  
2. Enters citizenship number  
3. Backend processes the image:
   - YOLO detects important regions  
   - OCR extracts text  
4. Extracted citizenship number is compared with user input  
5. Result is returned:

⚠️ Current Limitations
🔸 Only citizenship number verification is implemented
🔸 Name and gender matching not fully integrated
🔸 OCR accuracy depends on image quality
🔸 Model trained on limited dataset
🔸 Error handling and validation are basic
