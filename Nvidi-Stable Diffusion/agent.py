import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()

# For Stable Diffusion 3.5 Large
invoke_url = "https://ai.api.nvidia.com/v1/stabilityai/stable-diffusion-3-5-large"

# Get API key from environment
api_key = os.getenv("NVIDIA_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "prompt": "A beautiful sunset over mountains, high quality, detailed",
    "negative_prompt": "blurry, low quality, distorted",
    "cfg_scale": 7.5,
    "steps": 30,
    "seed": 0,
    "sampler": "euler",
    "height": 1024,
    "width": 1024
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    
    # The response contains base64 encoded image
    if 'artifacts' in data and len(data['artifacts']) > 0:
        image_b64 = data['artifacts'][0]['base64']
        image_bytes = base64.b64decode(image_b64)
        
        with open("generated_image.png", "wb") as f:
            f.write(image_bytes)
        print("Image saved as generated_image.png")
    else:
        print("No image in response")
        print(data)
else:
    print(f"Error: {response.text}")