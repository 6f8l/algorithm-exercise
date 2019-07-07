def main():
    alcoholism_sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    alcoholism_arr = alcoholism_sentence.split(' ')
    str_num = []
    for i in range(len(alcoholism_arr)):
        str_num.append(len(alcoholism_arr[i]))
    print(str_num)
    return

if __name__=='__main__':
    main()