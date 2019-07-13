import re

def replaceTabToSpace():
    with open('hightemp.txt', 'r') as file:
        text = re.sub(r'\t', '\s', file.read())
    print(text)
    return text

replaceTabToSpace()