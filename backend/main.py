from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from ai.image_gen import generate_image
from ai.face_swap import swap_face
from ai.video_gen import generate_video
from ai.upscaler import upscale_image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/image/gen")
async def image_gen_endpoint(prompt: str = Form(...)):
    path = await generate_image(prompt)
    return {"url": path}

@app.post("/api/image/upscale")
async def image_upscale_endpoint(file: UploadFile = File(...)):
    path = await upscale_image(file)
    return {"url": path}

@app.post("/api/face/swap")
async def face_swap_endpoint(file: UploadFile = File(...), ref_id: str = Form(...)):
    path = await swap_face(file, ref_id)
    return {"url": path}

@app.post("/api/video/gen")
async def video_gen_endpoint(prompt: str = Form(...), length: int = Form(5)):
    path = await generate_video(prompt, length)
    return {"url": path}
