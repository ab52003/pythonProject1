import re

class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.args = args


    def get_file_names(self):
        file_names = []
        for i in range(len(self.args)):
            name = self.args[i]
            with open(name, encoding='utf-8') as file:
                file_names.append(name)
        return file_names


    def get_all_words(self):
        all_words = {}
        a = ()
        b = ()
        for i in range(len(self.args)):
            name = self.args[i]
            with open(name, encoding='utf-8') as file:
                a = (str(name).lower())
                for y in file:
                    b = str(y).lower()
                    b = re.sub(r'[^\w\s]', '', b).split()
                    b = (b)
                all_words[a] = b
        return all_words


    def find(self, word):
        a = self.get_all_words()
        f = {}
        word = (str(word).lower())
        for name, words in a.items():
            if word in words:
                f[name] = words.index(word)
        return f


    def count(self, word):
        a = self.get_all_words()
        f = {}
        word = (str(word).lower())
        for name, words in a.items():
            if word in words:
                f[name] = words.count(word)
        return f

#w = WordsFinder('text_1.txt', 'text_2.txt', 'text_3.txt')

#print(w.get_all_words())

#print(w.get_file_names())

#print(w.find('с'))

#print(w.count('с'))

w = WordsFinder('test.txt')

print(w.get_all_words())

print(w.get_file_names())

print(w.find('TEXT'))

print(w.count('teXT'))