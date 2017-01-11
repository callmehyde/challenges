from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary_file:
        dictionary_list = dictionary_file.read().splitlines()
        return dictionary_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    sum_word = [LETTER_SCORES[letter.upper()] for letter in word
                if letter.upper() in LETTER_SCORES]
    return sum(sum_word)

def max_word_value(word_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_value_dict = {}
    for word in word_list:
        word_sum = calc_word_value(word)
        word_value_dict[word] = word_sum
    return max(word_value_dict, key=word_value_dict.get)

if __name__ == "__main__":
    MAX_VALUE = max_word_value()
    print(MAX_VALUE)
