import re

import requests
import uvicorn
import wget
from fastapi import FastAPI
from pydantic import BaseModel
from pytube import YouTube
from pytube.exceptions import PytubeError
from requests import ConnectionError, RequestException, Timeout

app = FastAPI()

SAVE_PATH = r"./"


class URL(BaseModel):
    url: str


@app.post('/download')
def download_content(request: URL):
    try:
        url = request.url
        if 'youtube' in url:
            YouTube(url).streams.first().download(SAVE_PATH)
        elif 'facebook' in url or 'fb' in url:
            html = requests.get(url)
            video_url = re.search('hd_src:"(.+?)"', html.text)
            if video_url:
                url = video_url[1].replace('hd_src:"', '')
            else:
                video_url = re.search('sd_src:"(.+?)"', html.text)
                if video_url:
                    url = video_url[1].replace('sd_src:"', '')

            wget.download(url, SAVE_PATH)
        return "Your video is downloaded", 200
    except (PytubeError, ConnectionError, RequestException, Timeout, TypeError) as e:
        return "There was an issue with your link", 500


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
