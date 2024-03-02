#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    print(
            'Body response:\n'
            f'\t- type: {type(html)}\n'
            f'\t- content: {html}\n'
            f'\t- utf8 content: {html.decode("utf-8")}'
        )
