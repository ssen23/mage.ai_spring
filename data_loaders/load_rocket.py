import requests
import os
import json
import requests.exceptions as requests_exceptions
import matplotlib.pyplot as plt
from PIL import Image

def download_launches():
    url = 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'
    os.makedirs("../rocket", exist_ok=True)
    response = requests.get(url)
    with open("../rocket/launches.json", "wb") as f:
        f.write(response.content)

download_launches()
def get_pictures(*args, **kwargs):
    os.makedirs("../image", exist_ok=True)
    with open("../rocket/launches.json", encoding='utf-8') as f:
        launches = json.load(f)
    image_urls = [launch["image"] for launch in launches["results"]]

    for image_url in image_urls:
        try:
            response = requests.get(image_url)
            image_filename = image_url.split("/")[-1]
            target_file = os.path.join("../image", image_filename)
            with open(target_file, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {image_url} to {target_file}")
        except requests_exceptions.MissingSchema:
            print(f"{image_url} appears to be an invalid URL.")
        except requests_exceptions.ConnectionError:
            print(f"Could not connect to {image_url}.")

get_pictures()
def notify(*args, **kwargs):
    images_count = len(os.listdir("../image"))
    if images_count > 0:
        print(f"There are now {images_count} images.")
    else :
        print("No images downloaded")
notify()

def visualize_images():
    image_folder = "../image"
    image_files = os.listdir(image_folder)
    num_images = len(image_files)
    num_cols = 4
    num_rows = (num_images // num_cols) + 1
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5*num_rows))
    for i, image_file in enumerate(image_files):
        row = i // num_cols
        col = i % num_cols
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        axes[row, col].imshow(image)
        axes[row, col].axis('off')
    plt.tight_layout()
    plt.show()
visualize_images()

