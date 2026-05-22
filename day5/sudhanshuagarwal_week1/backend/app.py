from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os

from models import User

# load env file
load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API URL from .env
API_URL = os.getenv("API_URL")


@app.get("/")
def home():
    return {"message": "Public API Explorer Backend Running"}


@app.get("/users")
def get_users():

    try:
        response = requests.get(API_URL, timeout=5)

        # raise error if request fails
        response.raise_for_status()

        data = response.json()

        users = []

        for item in data:

            user = User(
                id=item.get("id"),
                name=item.get("name"),
                email=item.get("email"),
                city=item.get("address", {}).get("city"),
                company=item.get("company", {}).get("name"),
            )

            users.append(user)

        return users

    except requests.exceptions.RequestException:
        return {
            "error": "Failed to fetch users"
        }

    except Exception as e:
        return {
            "error": str(e)
        }