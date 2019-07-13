def execute():
    with open('hightemp.txt') as f:
        lines = f.readlines()
    devided_lines = []
    for line in lines:
        devided_lines.append(line.split('\t'))
    col1_data = []
    col2_data = []
    for elem_arr in devided_lines:
        col1_data.append(elem_arr[0])
        col2_data.append(elem_arr[1])

    with open('./col1.txt', mode='w') as f:
        f.write(str(col1_data))

    with open('./col2.txt', mode='w') as f:
        f.write(str(col2_data))
execute()