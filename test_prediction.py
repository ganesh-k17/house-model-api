import requests

url = "https://house-model-api.onrender.com/predict" # site is deployed in render.com

data = {
    "size": 2000
}

response = requests.post(url, json=data)

print(response.json())