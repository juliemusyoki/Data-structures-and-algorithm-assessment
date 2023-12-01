import string

def word_frequency(sentence):
    frequency_dict = {}
    words = sentence.lower().split()

    for word in words:
        word = word.strip(string.punctuation)
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
