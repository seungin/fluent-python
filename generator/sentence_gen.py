import re
import reprlib

re_word = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re_word.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
