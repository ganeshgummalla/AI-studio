import os
import uuid
import asyncio
from moviepy.editor import ImageSequenceClip
from ai.image_gen import generate_image

async def generate_video(prompt: str, length: int) -> str:
    frame_count = length * 3
    tasks = [generate_image(f"{prompt} frame {i}") for i in range(frame_count)]
    paths = await asyncio.gather(*tasks)

    clip = ImageSequenceClip(paths, fps=3)
    out_dir = "outputs/videos"
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.mp4"
    out_path = os.path.join(out_dir, filename)
    clip.write_videofile(out_path, codec="libx264")

    return out_path
