import requests
import json

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

def downloader(url):
    res = requests.get(url,USER_AGENT)
    res.encoding = "big5"

    return res.text
