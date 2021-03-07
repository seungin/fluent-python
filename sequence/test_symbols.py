import array

symbols = "$¢£¥€¤"


def test_ordinal_values():
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    assert codes == [36, 162, 163, 165, 8364, 164]

    # list comprehension
    assert [ord(symbol) for symbol in symbols] == [36, 162, 163, 165, 8364, 164]

    # generator expression
    assert tuple(ord(s) for s in symbols) == (36, 162, 163, 165, 8364, 164)
    assert array.array("I", (ord(s) for s in symbols)) == array.array(
        "I", [36, 162, 163, 165, 8364, 164]
    )


def test_beyond_ascii():
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    assert beyond_ascii == [162, 163, 165, 8364, 164]
    assert beyond_ascii == list(filter(lambda c: c > 127, map(ord, symbols)))
