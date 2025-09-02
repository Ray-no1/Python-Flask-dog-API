import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# def get_dog_info():
#     url = f"https://api.thedogapi.com/v1/images/search"
#     headers = {
#         "x-api-key": os.getenv("API_KEY")
#     }
#     params = {
#         "mime_types": "jpg,png",
#         "has_breeds": "true",
#         "limit": 1
#     }
# response = requests.get(url, headers=headers, params=params).json()
# print(response)
# breed = f"{response[0]['breeds'][0]['name']}"
# weight = f"{response[0]['breeds'][0]['weight']['metric']} kilograms"
# height = f"{response[0]['breeds'][0]['height']['metric']} centimeters"
# bred_for = f"{response[0]['breeds'][0]['bred_for']}"
# lifespan = f"{response[0]['breeds'][0]['life_span']}"
# temperament = f"{response[0]['breeds'][0]['temperament']}"
# img_url = f"{response[0]['url']}"
# img_width = f"{response[0]['width']}"
# img_height = f"{response[0]['height']}"

# return breed, weight, height, bred_for, lifespan, temperament, img_url


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

    # dog_1 = dogs_info[0]


if __name__ == "__main__":
    get_dog_info()
