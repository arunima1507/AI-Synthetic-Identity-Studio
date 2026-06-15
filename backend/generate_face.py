import torch
import time

from training.generator import Generator
from torchvision.utils import save_image

device = torch.device("cpu")

generator = Generator()

generator.load_state_dict(
    torch.load(
        "models/generator_epoch_100.pth",
        map_location=device
    )
)

generator.eval()

def generate_face():
    
    noise = torch.randn(
        1,
        100,
        1,
        1
    )

    with torch.no_grad():

        fake_image = generator(noise)

    filename = f"generated_faces/face_{int(time.time())}.png"

    save_image(
        fake_image,
        filename,
        normalize=True
    )

    return filename