import re
import reprlib

re_word = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re_word.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
