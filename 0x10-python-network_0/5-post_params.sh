#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response
curl -s -d "email=email&subject=I+will+always+be+here+for+PLD" -X POST "$1"
