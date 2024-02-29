#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
curl -s "$1" | grep -q 200
