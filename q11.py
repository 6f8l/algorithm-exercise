# coding: utf-8

def judgeLineNum():
    num_lines = sum(1 for line in open('hightemp.txt'))
    return num_lines

print(judgeLineNum())