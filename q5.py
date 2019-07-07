def main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    arr = sentence.split(' ')
    one_str = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result_dict = {}
    for i in range(len(one_str)):
        one_str[i] = one_str[i] - 1

    for i in range(len(arr)):
        if i in one_str:
            result_dict[i] = arr[i][:1]
        else:
            result_dict[i] = arr[i][:2]
    print(result_dict)
    return result_dict

if __name__=='__main__':
    main()