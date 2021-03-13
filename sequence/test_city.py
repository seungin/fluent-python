from collections import OrderedDict
from collections import namedtuple

City = namedtuple("City", "name country population coordinates")


def test_city_tokyo():
    # namedtuple basics
    tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
    assert tokyo[0] == tokyo.name == "Tokyo"
    assert tokyo[1] == tokyo.country == "JP"
    assert tokyo[2] == tokyo.population == 36.933
    assert tokyo[3] == tokyo.coordinates == (35.689722, 139.691667)
    assert (
        repr(tokyo)
        == "City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))"
    )


def test_city_delhi():
    # namedtuple attribute and method
    assert City._fields == ("name", "country", "population", "coordinates")

    LatLong = namedtuple("LatLong", "lat long")
    delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(238.613889, 77.208889))
    delhi = City._make(delhi_data)
    assert delhi._asdict() == OrderedDict(
        [
            ("name", "Delhi NCR"),
            ("country", "IN"),
            ("population", 21.935),
            ("coordinates", LatLong(lat=238.613889, long=77.208889)),
        ]
    )
