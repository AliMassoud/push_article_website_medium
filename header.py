import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_headers() -> dict:
    """
    Get the headers for the medium request
    """
    # load json header
    with open("./models/header_medium.json", "r") as f:
        headers = json.load(f)
    # Load .env file
    token = os.getenv("TOKEN")
    # add token to header
    headers["Authorization"] = f"Bearer {token}"

    return headers


def get_author_id(headers: dict) -> str:
    """uses the /me medium api endpoint to get the user's author id"""
    response = requests.get(
        "https://api.medium.com/v1/me",
        headers=headers,
    )
    if response.status_code == 200:
        return response.json()["data"]["id"]
    else:
        raise Exception("Error getting author id")
