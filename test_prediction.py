import os
import requests

# url = "https://house-model-api.onrender.com/predict" # site is deployed in render.com
url = os.getenv("API_URL", "http://127.0.0.1:5000/predict")


data = {
    "size": 2000
}

response = requests.post(url, json=data)

print(response.json())