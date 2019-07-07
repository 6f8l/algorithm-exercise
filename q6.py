def main():
    n = 2
    sentence = "I am an NLPer"
    arr = sentence.split()
    result = []
    def bi_gram(n):
        for i, c in enumerate(arr):
            if i + n > len(sentence):
                return result
            print(arr[i: i+n])
            result.append(arr[i: i+n])
        print(result)
        return result
    return bi_gram(n)

if __name__=='__main__':
    main()