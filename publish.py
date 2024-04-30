# python publish.py "input/about.md" --title 'about me page9'
import argparse

import click
import pyperclip
import requests

from content_prep import prep_data
from header import get_author_id, get_headers
from images import extract_images, publish_image

# 1. Add type hinting + fix naming issues (Done)
# 2. Remove Hugo Markdown beginning syntax
# 3. Add Try/Except block to handle errors (Done)
# 4. Add Click to handle CLI arguments instead of argparse (Done)
# 5. Force adding tags (Done)
# 6. Create .sh file to do the following:
# - push article to medium
# - then move article to certain folder with its images (the folder name should be posts/<article_name>/index.md + images)
# - then push the changes to the repo (to sync with the website on Github Pages)
# 7. Add a check to see if the article is already published on Medium
# 9.


def copy_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


def post_article(data: dict, base_path: str) -> str:
    """
    Posts an article to medium with the input payload
    Parameters:
    data, dict: The payload to post.
    base_path, str: The base path of the images related to the post.
    """
    headers = get_headers()
    images_path = extract_images(data["content"])
    for image_path in images_path:
        new_url = publish_image(f"{base_path}/{image_path}", headers)
        if new_url is not None:
            # Put the url instead of the original images
            data["content"] = data["content"].replace(image_path, new_url)
    author_id = get_author_id(headers)
    url = "https://api.medium.com/v1/users/{}/posts".format(author_id)
    response = requests.request("post", url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        response_json = response.json()
        # get the URL of the uploaded post
        medium_post_url = response_json["data"]["url"]
        return medium_post_url
    else:
        raise Exception("Error posting article")


@click.command()
@click.argument("filepath", type=click.Path(exists=True), required=True)
@click.option("-t", "--title", required=True, help="title of post", type=str)
@click.option("-a", "--tags", required=True, help="tags, separated by ','", type=str)
@click.option(
    "-p",
    "--pub",
    required=False,
    help="publish status, one of draft/unlisted/public, defaults to draft",
    default="draft",
    show_default=True,
    type=click.Choice(["public", "unlisted", "draft"]),
)
def main(
    filepath: str,
    title: str,
    tags: str = None,
    pub: str = None,
):
    args = {
        "filepath": filepath,
        "title": title,
        "tags": tags,
        "pub": pub,
    }
    data = prep_data(args)
    post_url = post_article(data, "./input/images/")
    copy_to_clipboard(post_url)
    print(post_url)


if __name__ == "__main__":
    main()
