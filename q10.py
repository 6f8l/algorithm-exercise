import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def execute(sentence):
    """
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ
    ただし，長さが４以下の単語は並び替えないこととする.
    適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与えその実行結果を確認せよ．
    """
    arr = sentence.split(' ')
    for word in arr:
        word_len = len(word)
        if word_len >= 4:
            init_str = word[0:1]
            final_str = word[word_len - 1:word_len]
            # for i in range()
        else:
            pass


execute(sentence)