#coding utf-8

def displayLine(file, N):
    with open(file) as f:
        lines = f.readlines()

    if N > len(lines):
        print('呼び出しの行数が多すぎます')
        exit

    for i in range(0, N):
        print(lines[i])
    return lines

file = 'hightemp.txt'

print('\n何行呼び出しますか？')
N = int(input())

displayLine(file, N)