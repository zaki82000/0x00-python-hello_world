#!/usr/bin/python3
# Python script that fetches URL.
from urllib.request import urlopen


with urlopen('https://intranet.alxswe.com/status') as response:
    html = response.read()

html
