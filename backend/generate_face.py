import torch

from training.generator import Generator
from torchvision.utils import save_image

device = torch.device("cpu")

generator = Generator()

generator.load_state_dict(
    torch.load(
        "models/generator.pth",
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

    save_image(
        fake_image,
        "generated_faces/api_face.png",
        normalize=True
    )

    return "generated_faces/api_face.png"