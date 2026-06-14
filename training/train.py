# Imports

import torch
import torch.nn as nn
import csv
from torchvision.utils import save_image
from torch.utils.data import DataLoader

from dataset import (
    CelebADataset,
    transform
)

from generator import Generator
from discriminator import Discriminator


# Config

DATASET_PATH = "celeba_hq_256"

BATCH_SIZE = 128

LATENT_DIM = 100

LEARNING_RATE = 0.0002

EPOCHS = 2


# Dataset

dataset = CelebADataset(
    DATASET_PATH,
    transform=transform
)
dataset.images = dataset.images[:1000]

dataloader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

print("Dataset Loaded")
print("Images:", len(dataset))


# Device

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(device)


# Models

generator = Generator().to(device)

discriminator = Discriminator().to(device)

print("Models Created")


# Loss Function

criterion = nn.BCELoss()


# Optimizers

optimizer_g = torch.optim.Adam(
    generator.parameters(),
    lr=LEARNING_RATE,
    betas=(0.5, 0.999)
)

optimizer_d = torch.optim.Adam(
    discriminator.parameters(),
    lr=LEARNING_RATE,
    betas=(0.5, 0.999)
)

real_label = 1.
fake_label = 0.

fixed_noise = torch.randn(
    16,
    LATENT_DIM,
    1,
    1,
    device=device
)

with open("training/losses.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "epoch",
        "loss_d",
        "loss_g"
    ])

for epoch in range(EPOCHS):
    
    for i, real_images in enumerate(dataloader):

        real_images = real_images.to(device)

        batch_size = real_images.size(0)

        real_labels = torch.full(
            (batch_size,),
            real_label,
            device=device
        )

        fake_labels = torch.full(
            (batch_size,),
            fake_label,
            device=device
        )

        # Train Discriminator

        discriminator.zero_grad()

        output_real = discriminator(
            real_images
        ).view(-1)

        loss_real = criterion(
            output_real,
            real_labels
        )

        loss_real.backward()

        noise = torch.randn(
            batch_size,
            LATENT_DIM,
            1,
            1,
            device=device
        )

        fake_images = generator(noise)

        output_fake = discriminator(
            fake_images.detach()
        ).view(-1)

        loss_fake = criterion(
            output_fake,
            fake_labels
        )

        loss_fake.backward()

        optimizer_d.step()

        # Train Generator

        generator.zero_grad()

        output = discriminator(
            fake_images
        ).view(-1)

        loss_g = criterion(
            output,
            real_labels
        )

        loss_g.backward()

        optimizer_g.step()

        if i % 10 == 0:

            print(
                f"Epoch [{epoch+1}/{EPOCHS}] "
                f"Batch [{i}] "
                f"Loss D: {(loss_real + loss_fake).item():.4f} "
                f"Loss G: {loss_g.item():.4f}"
            )
    with torch.no_grad():

        fake = generator(
            fixed_noise
        )

        save_image(
            fake,
            f"generated_faces/epoch_{epoch+1}.png",
            normalize=True
        )

        torch.save(
            generator.state_dict(),
            f"models/generator_epoch_{epoch+1}.pth"
        )

        torch.save(
            discriminator.state_dict(),
            f"models/discriminator_epoch_{epoch+1}.pth"
        )
    
    with open("training/losses.csv", "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            epoch + 1,
            (loss_real + loss_fake).item(),
            loss_g.item()
        ])


torch.save(
    generator.state_dict(),
    "models/generator.pth"
)

torch.save(
    discriminator.state_dict(),
    "models/discriminator.pth"
)

print("Models Saved")