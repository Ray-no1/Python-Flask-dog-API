import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_dog_info():
    url = f"https://api.thedogapi.com/v1/images/search"
    headers = {
        "x-api-key": os.getenv("API_KEY")
    }
    params = {
        "mime_types": "jpg,png",
        "has_breeds": "true",
        "limit": 10,
        "page": 1
    }
    dogs_info = requests.get(url, headers=headers, params=params).json()
    dogs = []
    for dog in dogs_info:
        breed_info = dog['breeds'][0]
        if breed_info.get('bred_for') and breed_info.get('breed_group') and breed_info.get('life_span'):
            dogs.append({
                "weight": breed_info['weight']['metric'],
                "height": breed_info['height']['metric'],
                "name": breed_info['name'],
                "bred_for": breed_info.get('bred_for', 'N/A'),
                "breed_group": breed_info.get('breed_group', 'N/A'),
                "life_span": breed_info.get('life_span', 'N/A'),
                "temperament": breed_info.get('temperament', 'N/A'),
                "url": dog['url']
            })
    return dogs


if __name__ == "__main__":
    get_dog_info()
