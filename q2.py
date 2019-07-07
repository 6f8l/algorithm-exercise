def main():
    s = 'パタトクカシーー'
    arr = list(s)
    ans_arr = []
    for i in range(len(arr)):
        if i % 2 == 0:
            pass
        elif i % 2 == 1:
            ans_arr.append(arr[i])
        else:
            print('error')

    ans = ''.join(ans_arr)
    print(ans)
    return ans

if __name__=='__main__':
    main()