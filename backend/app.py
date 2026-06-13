from fastapi import FastAPI
from faker import Faker

app = FastAPI()
fake = Faker()

@app.get("/")
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

    return profile

def home():

    return {
        "message": "AI Synthetic Identity Studio API Running"
    }