import os
import uuid
import tempfile
import cv2
from realesrgan import RealESRGAN

def get_upscaler():
    device = "cuda" if cv2.cuda.getCudaEnabledDeviceCount() > 0 else "cpu"
    model = RealESRGAN(device, scale=4)
    model.load_weights("weights/RealESRGAN_x4.pth")
    return model

upscaler = get_upscaler()

async def upscale_image(file) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    contents = await file.read()
    tmp.write(contents)
    tmp.flush()

    img = cv2.imread(tmp.name)
    result = upscaler.enhance(img)

    out_dir = "outputs/upscaled"
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    out_path = os.path.join(out_dir, filename)
    cv2.imwrite(out_path, result)

    tmp.close()
    return out_path
