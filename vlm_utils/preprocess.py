from PIL import Image
import torch

def prepare_image(image_path, size=336):
    """Prepare image for VLM input."""
    img = Image.open(image_path).convert('RGB')
    img = img.resize((size, size))
    return img
