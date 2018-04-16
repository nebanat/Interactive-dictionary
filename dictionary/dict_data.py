import json


def load_data_to_dict():
    dictionary = json.load(open('data.json'))
    return dictionary
