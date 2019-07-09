# coding: utf-8

sentence = input()

def cipher(sentence):
    modified_s = ""
    for o in sentence:
        if o.islower():
            modified_s += chr(219 - ord(o))
        else:
            modified_s += o

    return modified_s

print(cipher(sentence))