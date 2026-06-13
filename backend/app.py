from fastapi import FastAPI
from faker import Faker
from backend.generate_face import generate_face

app = FastAPI()
fake = Faker()


@app.get("/generate-profile")
def generate_profile():

    return {
        "name": fake.name(),
        "age": fake.random_int(
            min=18,
            max=65
        ),
        "occupation": fake.job(),
        "city": fake.city(),
        "email": fake.email()
    }

@app.get("/generate-identity")
def generate_identity():

    image_path = generate_face()

    profile = {
        "name": fake.name(),
        "age": fake.random_int(
            min=18,
            max=65
        ),
        "occupation": fake.job(),
        "city": fake.city(),
        "email": fake.email()
    }

    return {
        "profile": profile,
        "image_path": image_path
    }

@app.get("/generate-face")
def generate_face_api():

    image_path = generate_face()

    return {
        "image_path": image_path
    }

@app.get("/")
def home():

    return {
        "message": "AI Synthetic Identity Studio API Running"
    }