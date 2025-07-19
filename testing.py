import requests
from dotenv import load_dotenv
import os
from PIL import Image
import BytesIO

# load_dotenv()
# plant_key = os.getenv("plant_key")

# url = f"https://my-api.plantnet.org/v2/identify/all?api-key={plant_key}"

# img_path = "aster.jpeg"
# files = {
#     "images": (img_path, open(img_path, "rb"))
# }
# data = {
# }
# response = requests.post(url, files=files, data=data) #multi part send thing. in the api files is in form data
# print(response.status_code)

# if response.status_code == 200:
#     results = response.json().get("results", [])
#     print(results)
# else:
#     print(response.text) 
response = requests.get(img_url)
img = Image.open(BytesIO(response.content)) #get image 
pred = predict(model, img, should_log=True)