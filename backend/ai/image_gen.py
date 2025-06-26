import os
import uuid
import torch
from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline = pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

def save_image(image, filename: str) -> str:
    out_dir = "outputs/images"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    image.save(path)
    return path

async def generate_image(prompt: str) -> str:
    image = pipeline(prompt).images[0]
    filename = f"{uuid.uuid4().hex}.png"
    return save_image(image, filename)
