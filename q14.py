def readline_file(file):
    with open(file, 'r') as f:
        return f.readlines()

def save_file(file, text):
    with open(file, 'w') as f:
        f.write(text)

col1 = readline_file('col1.txt')
col2 = readline_file('col2.txt')

col1 = list(map(lambda x: x.strip(), col1))
col2 = list(map(lambda x: x.strip(), col2))

lines = ["{0}\t{1}".format(line1, line2) for line1, line2 in zip(col1, col2)]

save_file('marge.txt', ''.join(lines))