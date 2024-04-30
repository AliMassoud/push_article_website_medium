from pathlib import Path

import markdown
import requests
from bs4 import BeautifulSoup


def publish_image(image_path: str, headers: dict) -> dict:
    """
    Publish a single image on the medium
    parameters:
    image_path, str: The path to the image
    headers, dict: The headers for the medium request to publish the image
    """
    # Open image
    with open(image_path, "rb") as f:
        filename = Path(image_path).name
        extension = image_path.split(".")[-1]
        content_type = f"image/{extension}"
        files = {"image": (filename, f, content_type)}
        url = "https://api.medium.com/v1/images"
        response = requests.request("post", url, headers=headers, files=files)
        if 200 <= response.status_code < 300:
            try:
                json = response.json()
                return json["data"]["url"]
            except KeyError:
                return json


def extract_images(content: str) -> list:
    """
    Extract images from the content of a post, by parsing the markdown content to html and extracting the images.
    parameters:
    content, str: The content of the post
    """
    output = markdown.markdown(content)
    soup = BeautifulSoup(output, "html.parser")
    imgs_extracted_html = soup.find_all("img")
    imgs_extracted_list = []
    for image in imgs_extracted_html:
        imgs_extracted_list.append(image["src"])
    return imgs_extracted_list
