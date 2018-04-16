from difflib import get_close_matches
from dictionary.dict_data import load_data_to_dict

our_dictionary = load_data_to_dict()


def get_dictionary_meaning():
    word = input('Please enter the word you want to search: ')
    word = word.strip().lower()
    proper_word = word.strip().title()
    caps_word = word.strip().upper()

    if word in our_dictionary:
        return word_meaning(our_dictionary[word])
    elif proper_word in our_dictionary:
        return word_meaning(our_dictionary[proper_word])
    elif caps_word in our_dictionary:
        return word_meaning(our_dictionary[caps_word])
    else:
        close_matches = get_close_matches(word, our_dictionary.keys(), cutoff=0.7)
        if len(close_matches) > 0:
            answer = input('Do you mean {} instead. Enter Y/N?'.format(close_matches[0]))
            return get_word_suggestions(answer, close_matches[0], word)
        else:
            return '{} does not exist'.format(word)


def get_word_suggestions(ans, close_match, word):
    if ans.lower() in ['y', 'yes']:
        return word_meaning(our_dictionary[close_match])
    elif ans.lower() in ['n', 'no']:
        return '{} does not exist'.format(word)
    else:
        return 'We do not understand your input'


def word_meaning(result_dict):
    for result in result_dict:
            print(result)
    return ''


if __name__ == '__main__':
    print(get_dictionary_meaning())


