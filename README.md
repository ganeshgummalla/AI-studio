# AI Studio

This application provides:
- AI Image Generation (Diffusers)
- Face Swap (DeepFace)
- Video Generation (FFmpeg + frames)
- Image Upscaling (Real-ESRGAN)

## Setup

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
