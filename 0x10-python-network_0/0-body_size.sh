#!/bin/bash
#Bash script that takes in a URL
curl -s -o /dev/null -w "%{size_download}\n" $1