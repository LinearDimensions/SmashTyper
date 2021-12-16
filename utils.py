from collections import defaultdict

def load_dict():
    data_dct = defaultdict(list)
    with open("30k.txt") as file:
        data = file.read()
        data_list = data.split('\t\n')
        for i in data_list:
            data_dct[frozenset(i.lower())].append(i.lower())
        return data_dct

def posStr(word,word_dict): # using machine learning, sort by probability
    if word_dict[frozenset(word)]:
        return word_dict[frozenset(word)]
    else:
        return [word]