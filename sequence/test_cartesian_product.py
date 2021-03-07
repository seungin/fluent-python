colors = ["black", "white"]
sizes = ["S", "M", "L"]


def test_t_shirts():
    # list comprehension
    t_shirts = [(color, size) for color in colors for size in sizes]
    assert t_shirts == [
        ("black", "S"),
        ("black", "M"),
        ("black", "L"),
        ("white", "S"),
        ("white", "M"),
        ("white", "L"),
    ]

    # generator expression
    t_shirts = tuple("%s %s" % (c, s) for c in colors for s in sizes)
    assert t_shirts == (
        "black S",
        "black M",
        "black L",
        "white S",
        "white M",
        "white L",
    )
