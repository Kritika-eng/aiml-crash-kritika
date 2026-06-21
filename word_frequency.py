def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

sentence = "python is fun and python is easy"
print(word_frequency(sentence))
