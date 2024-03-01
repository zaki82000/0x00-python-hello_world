#!/usr/bin/python3
# Python script that fetches URL.
import urllib.request


with urllib.request.urlopen('https://intranet.alxswe.com/status') as response:
    html = response.read()
print("Body response:")
print("    - type: {}".format(type(html)))
print("    - content: {}".format(html))
print("    - utf8 content: {}".format(html.decode('utf-8')))