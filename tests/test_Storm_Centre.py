from Storm_Centre import Storm_Centre
from Storm import Storm
from Tornado import Tornado
from Blizzard import Blizzard
from Hurricane import Hurricane


def test_create_storm_centre():
    c1 = Storm_Centre()
    assert c1.storm_list == []


def test_already_exists():
    c1 = Storm_Centre()
    assert c1.already_exists("Test1") is False
    c1.storm_list.append(Hurricane("Test2", 100))
    assert c1.already_exists("Test2") is True


def test_centre_add_hurricane():
    c1 = Storm_Centre()
    h1 = Hurricane("TestHurricane", 40)
    c1.add_storm(h1)
    assert c1.storm_list == [h1]


def test_centre_add_tornado():
    c1 = Storm_Centre()
    t1 = Tornado("TestTornado", 40)
    c1.add_storm(t1)
    assert c1.storm_list == [t1]


def test_centre_add_blizzard():
    c1 = Storm_Centre()
    b1 = Blizzard("TestBlizzard", 40, 10)
    c1.add_storm(b1)
    assert c1.storm_list == [b1]


def test_add_unspecified_storm():
    class NewStorm(Storm):
        def __init__(self, name, wind_speed):
            super().__init__(name, wind_speed)

        def calculate_classification(self):
            pass

        def get_advice(self):
            pass

    c1 = Storm_Centre()
    s1 = NewStorm("testStorm", 40)
    assert c1.add_storm(s1) is False


def test_repeated_name():
    c1 = Storm_Centre()
    h1 = Hurricane("TestHurricane", 40)
    h2 = Hurricane("TestHurricane", 40)
    assert c1.add_storm(h1) is True
    assert c1.add_storm(h2) is False


def test_maximum_capacity():
    c1 = Storm_Centre()
    h1 = Hurricane("TestHurricane1", 40)
    h2 = Hurricane("TestHurricane2", 40)
    h3 = Hurricane("TestHurricane3", 40)
    h4 = Hurricane("TestHurricane4", 40)
    h5 = Hurricane("TestHurricane5", 40)
    h6 = Hurricane("TestHurricane6", 40)
    h7 = Hurricane("TestHurricane7", 40)
    h8 = Hurricane("TestHurricane8", 40)
    h9 = Hurricane("TestHurricane9", 40)
    h10 = Hurricane("TestHurricane10", 40)
    h11 = Hurricane("TestHurricane11", 40)
    h12 = Hurricane("TestHurricane12", 40)
    h13 = Hurricane("TestHurricane13", 40)
    h14 = Hurricane("TestHurricane14", 40)
    h15 = Hurricane("TestHurricane15", 40)
    h16 = Hurricane("TestHurricane16", 40)
    h17 = Hurricane("TestHurricane17", 40)
    h18 = Hurricane("TestHurricane18", 40)
    h19 = Hurricane("TestHurricane19", 40)
    h20 = Hurricane("TestHurricane20", 40)
    h21 = Hurricane("TestHurricane21", 40)
    assert c1.add_storm(h1) is True
    assert c1.add_storm(h2) is True
    assert c1.add_storm(h3) is True
    assert c1.add_storm(h4) is True
    assert c1.add_storm(h5) is True
    assert c1.add_storm(h6) is True
    assert c1.add_storm(h7) is True
    assert c1.add_storm(h8) is True
    assert c1.add_storm(h9) is True
    assert c1.add_storm(h10) is True
    assert c1.add_storm(h11) is True
    assert c1.add_storm(h12) is True
    assert c1.add_storm(h13) is True
    assert c1.add_storm(h14) is True
    assert c1.add_storm(h15) is True
    assert c1.add_storm(h16) is True
    assert c1.add_storm(h17) is True
    assert c1.add_storm(h18) is True
    assert c1.add_storm(h19) is True
    assert c1.add_storm(h20) is True
    assert c1.add_storm(h21) is False


def test_remove_real_storm():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.remove_storm("testHurricane") is True
    assert c1.storm_list == []


def test_remove_not_real_storm():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.remove_storm("testHurricane1") is False
    assert c1.storm_list == [h1]


def test_view_real_storm():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.view_storm("testHurricane") == h1


def test_view_not_real_storm():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.view_storm("test") is None


def test_update_real_hurricane():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.update_storm("testHurricane", {
        "windspeed": 50
    }) is True
    assert c1.storm_list[0].wind_speed == 50


def test_update_fake_hurricane():
    c1 = Storm_Centre()
    h1 = Hurricane("testHurricane", 40)
    c1.add_storm(h1)
    assert c1.update_storm("test", {
        "windspeed": 50
    }) is False
    assert c1.storm_list[0].wind_speed == 40


def test_update_real_blizzard():
    c1 = Storm_Centre()
    b1 = Blizzard("testBlizzard", 40, 10)
    c1.add_storm(b1)
    assert c1.update_storm("testBlizzard", {
        "windspeed": 50,
        "temp": -10
    }) is True
    assert c1.storm_list[0].wind_speed == 50
    assert c1.storm_list[0].temp == -10


def test_update_not_real_blizzard():
    c1 = Storm_Centre()
    b1 = Blizzard("testBlizzard", 40, 10)
    c1.add_storm(b1)
    assert c1.update_storm("test", {
        "windspeed": 50,
        "temp": -10
    }) is False
    assert c1.storm_list[0].wind_speed == 40
    assert c1.storm_list[0].temp == 10
