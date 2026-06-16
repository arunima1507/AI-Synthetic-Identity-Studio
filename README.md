# AI Synthetic Identity Studio

## Overview

AI Synthetic Identity Studio is a full-stack machine learning application that generates realistic synthetic human identities using a Deep Convolutional Generative Adversarial Network (DCGAN).

The system combines AI-generated face images with synthetic demographic information to create privacy-preserving identities that can be used for:

- Software Testing
- UI/UX Prototyping
- Machine Learning Research
- Educational Demonstrations
- Synthetic Dataset Generation

No real personal information is used or stored.

---

## Problem Statement

Access to realistic human data is often limited by privacy regulations, ethical concerns, and legal restrictions.

This project addresses that challenge by generating synthetic identities consisting of:

- AI-generated face images
- Synthetic names
- Synthetic demographic information

allowing developers and researchers to work with realistic-looking data without exposing real individuals.

---

## Features

### Synthetic Face Generation

- DCGAN-based face generation
- Trained on the CelebA-HQ dataset
- Generates unique synthetic human faces

### Identity Generation

Each identity includes:

- Name
- Age
- Occupation
- City
- Email Address
- AI-generated Face

### Dataset Generation

Generate:

- 10 identities
- 50 identities
- 100 identities

in a single click.

### Export Options

- JSON Export
- CSV Dataset Export
- Identity Card Export

### History Tracking

- Stores previously generated identities
- Allows reloading older identities

### Machine Learning Dashboard

Displays:

- Model Architecture
- Dataset Information
- Training Duration
- Training Evolution Gallery
- GAN Loss Graph

---

## Machine Learning Pipeline

### Dataset

CelebA-HQ Dataset

- ~30,000 facial images
- Preprocessed to 64×64 resolution

### Model

Deep Convolutional Generative Adversarial Network (DCGAN)

Components:

- Generator Network
- Discriminator Network

### Training Configuration

| Parameter | Value |
|------------|------------|
| Dataset | CelebA-HQ |
| Resolution | 64 × 64 |
| Epochs | 100 |
| Device | CPU |
| Training Time | ~18 Hours |

---

## Training Results

The model was trained for 100 epochs.

Training progression demonstrates:

- Early epochs: random noise
- Mid epochs: rough facial structures
- Late epochs: realistic human faces

The application includes:

- Training Evolution Gallery
- Generator vs Discriminator Loss Graph

for visual analysis of model performance.

---

## Technology Stack

### Machine Learning

- PyTorch
- TorchVision
- NumPy
- Matplotlib

### Backend

- FastAPI
- Faker

### Frontend

- HTML
- CSS
- JavaScript

### Version Control

- Git
- GitHub

---

## Project Structure

```text
backend/
    app.py
    generate_face.py

frontend/
    index.html
    style.css
    script.js

training/
    generator.py
    discriminator.py
    train.py
    dataset.py

analytics/
    loss_graph.py
    loss_graph.png

generated_faces/
generated_identities/

models/
```

---

## How To Run

### Clone Repository

```bash
git clone <repository-url>
cd AI-Synthetic-Identity-Studio
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Backend

```bash
uvicorn backend.app:app --reload
```

### Open Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## Sample Workflow

1. Generate a synthetic identity
2. View generated face and profile
3. Save identity as JSON
4. Generate datasets in bulk
5. Export CSV datasets
6. Explore training analytics

---

## Future Improvements

- Higher resolution GAN training
- StyleGAN integration
- Cloud deployment
- User authentication
- Synthetic identity quality scoring
- Real-time training monitoring

---

## Author

Arunima

AI / Machine Learning Portfolio Project