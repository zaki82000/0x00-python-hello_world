#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.
"""
from urllib.request import urlopen 
from sys import argv

with urlopen(argv[1]) as response :
    id = response.getheader('X-Request-Id')

print(id)