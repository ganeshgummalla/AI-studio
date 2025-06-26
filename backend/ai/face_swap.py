import os
import uuid
import cv2
import tempfile
from deepface import DeepFace

async def swap_face(file, ref_id: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    contents = await file.read()
    tmp.write(contents)
    tmp.flush()

    ref_path = os.path.join("ai_models/characters", f"{ref_id}.jpg")
    swapped = DeepFace.swap(img_path=tmp.name, dest_path=ref_path)
    tmp.close()

    return swapped
