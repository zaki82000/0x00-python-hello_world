#!/usr/bin/python3
"""
function that prints a text
with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text
    with 2 new lines after each of these characters: ., ? and :

    arg:
        text: is text to print

    rasies:
        TypeError: text must be a string
    """
    characters_list = ['.', ':', '?']
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in characters_list:
        text = text.replace(char, char + '\n\n')

    print(text)
