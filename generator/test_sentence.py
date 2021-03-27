from generator import sentence
from generator import sentence_gen
from generator import sentence_gen2
from generator import sentence_genexp
from generator import sentence_iter


def test_sentence():
    __test_sentence(sentence.Sentence('"The time has come," the Walrus said,'))
    __test_sentence(sentence_iter.Sentence('"The time has come," the Walrus said,'))
    __test_sentence(sentence_gen.Sentence('"The time has come," the Walrus said,'))
    __test_sentence(sentence_gen2.Sentence('"The time has come," the Walrus said,'))
    __test_sentence(sentence_genexp.Sentence('"The time has come," the Walrus said,'))


def __test_sentence(s):
    assert repr(s) == "Sentence('\"The time ha... Walrus said,')"

    expected_words = (
        word for word in ("The", "time", "has", "come", "the", "Walrus", "said")
    )
    for word in s:
        assert next(expected_words) == word

    assert list(s) == ["The", "time", "has", "come", "the", "Walrus", "said"]
