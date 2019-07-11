import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def execute(sentence):
    arr = sentence.split(' ')
    result_arr = []
    for word in arr:
        word_len = len(word)
        if word_len >= 4:
            init_str = word[0:1]
            final_str = word[word_len - 1:word_len]
            other_strs = word[1:word_len - 1]
            other_strs_arr = random.sample(other_strs, len(other_strs))
            word = init_str + ''.join(other_strs_arr) + final_str
            result_arr.append(word)
        else:
            result_arr.append(word)
        # append space to devide sentence by space.
        result_arr.append(' ')

    result_str = ''.join(result_arr)
    print(result_str)
    return result_str

execute(sentence)