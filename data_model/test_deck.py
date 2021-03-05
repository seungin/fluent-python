from random import choice

import pytest

from data_model.deck import Card
from data_model.deck import FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()


def test_french_deck(deck):
    assert len(deck) == 52
    assert deck[0] == Card("2", "spades")
    assert deck[-1] == Card("A", "hearts")
    assert deck[:3] == [Card("2", "spades"), Card("3", "spades"), Card("4", "spades")]
    assert choice(deck) in deck
    assert Card("7", "beasts") not in deck
