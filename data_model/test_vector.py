from data_model.vector import Vector


def test_vector():
    v0 = Vector()
    v1 = Vector(1, 2)
    v2 = Vector(2, 2)
    v3 = Vector(3, 4)

    assert repr(v0) == "Vector(0, 0)"
    assert abs(v3) == 5
    assert abs(v1 + v2) == abs(v3)
    assert abs(v3 * 3) == 15
    assert not bool(v0)
    assert bool(v1)
