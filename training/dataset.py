import os
from PIL import Image

from torch.utils.data import Dataset
from torchvision import transforms


transform = transforms.Compose([
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.5,0.5,0.5],
        [0.5,0.5,0.5]
    )
])


class CelebADataset(Dataset):

    def __init__(self, folder_path, transform=None):

        self.folder_path = folder_path
        self.transform = transform

        self.images = [
            file for file in os.listdir(folder_path)
            if file.endswith((".jpg",".jpeg",".png"))
        ]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        image_path = os.path.join(
            self.folder_path,
            self.images[idx]
        )

        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image