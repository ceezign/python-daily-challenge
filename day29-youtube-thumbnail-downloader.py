# Youtube Thumbnail Downloader

import re
import os
import requests
from PIL import Image
from io import BytesIO

# to extract video ID

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    Supports formats like:
      - https://www.youtube.com/watch?v=abc123
      - https://youtu.be/abc123
      - https://www.youtube.com/shorts/abc123
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Invalid Youtube URL: {url}")

# To download the thumbnail
def download_thumbnail(video_url, qualities=None, output_folder="thumbnails"):
    try:
        video_id = extract_video_id(video_url)
    except ValueError as e:
        print(e)
        return

    if qualities is None:
        qualities = ["maxresdefault", "hqdefault", "mqdefault", "default"]

    os.makedirs(output_folder, exist_ok=True)

    for quality in qualities:
        image_url = f"https://img.youtube.com/vi/{video_id}/{quality}.jpg"
        try:
            response = requests.get(image_url, timeout=10)
            if response.status_code == 200:
                image_name = f"{video_id}_{quality}.jpg"
                image_path = os.path.join(output_folder, image_name)
                with open(image_path, "wb") as file:
                    file.write(response.content)

                image = Image.open(BytesIO(response.content))
                width, height = image.size
                print(f"Downloaded {image_name} ({width}x{height})")
            else:
                print(f"Could not fetch {quality} thumbnail for {video_id}")
        except Exception as err:
            print(f"Error download {quality} thumbnails: {err}")

if __name__ == "__main__":
    # Single video
    single_video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_thumbnail(single_video_url)

    # multiple videos
    multiple_urls = [
        "https://youtu.be/tPEE9ZwTmy0",
        "https://www.youtube.com/watch?v=aqz-KE-bpKQ",
        "https://www.youtube.com/shorts/8ybW48rKBME"
    ]

    print("\n--- Downloading multiple videos ---\n")
    for url in multiple_urls:
        download_thumbnail(url)


