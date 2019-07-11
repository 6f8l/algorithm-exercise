import re

def replaceTabToSpace():
    with open('hightemp.txt', 'r') as file:
        text = re.sub(r'\t', '\s', file.read())
    print(text)
    return text


# TODO: Create function that confirm result is correct or incorrect.
# def confirmResult():
#     return 'something'

replaceTabToSpace()