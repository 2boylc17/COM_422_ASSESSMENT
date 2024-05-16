import pytest
from Tornado import Tornado


def test_create_tornado():
    t1 = Tornado("testTornado", 100)
    assert t1.name == "testTornado" and t1.wind_speed == 100


def test_classify_tornado_category_0():
    t1 = Tornado("testTornado", 40)
    t2 = Tornado("testTornado", 55)
    t3 = Tornado("testTornado", 72)
    assert t1.calculate_classification() == "F0"
    assert t2.calculate_classification() == "F0"
    assert t3.calculate_classification() == "F0"


def test_classify_tornado_category_1():
    t1 = Tornado("testTornado", 73)
    t2 = Tornado("testTornado", 100)
    t3 = Tornado("testTornado", 112)
    assert t1.calculate_classification() == "F1"
    assert t2.calculate_classification() == "F1"
    assert t3.calculate_classification() == "F1"


def test_classify_tornado_category_2():
    t1 = Tornado("testTornado", 113)
    t2 = Tornado("testTornado", 130)
    t3 = Tornado("testTornado", 157)
    assert t1.calculate_classification() == "F2"
    assert t2.calculate_classification() == "F2"
    assert t3.calculate_classification() == "F2"


def test_classify_tornado_category_3():
    t1 = Tornado("testTornado", 158)
    t2 = Tornado("testTornado", 180)
    t3 = Tornado("testTornado", 205)
    assert t1.calculate_classification() == "F3"
    assert t2.calculate_classification() == "F3"
    assert t3.calculate_classification() == "F3"


def test_classify_tornado_category_4():
    t1 = Tornado("testTornado", 206)
    t2 = Tornado("testTornado", 240)
    t3 = Tornado("testTornado", 260)
    assert t1.calculate_classification() == "F4"
    assert t2.calculate_classification() == "F4"
    assert t3.calculate_classification() == "F4"


def test_classify_tornado_category_5():
    t1 = Tornado("testTornado", 261)
    t2 = Tornado("testTornado", 9999)
    assert t1.calculate_classification() == "F5"
    assert t2.calculate_classification() == "F5"


def test_classify_tornado_unclassified():
    t1 = Tornado("testTornado", 39)
    assert t1.calculate_classification() == "Unclassified"


def test_get_advice_shield_yourself():
    t1 = Tornado("testTornado", 40)
    t2 = Tornado("testTornado", 73)
    assert t1.get_advice() == "Find safe room/shelter, shield yourself from debris"
    assert t2.get_advice() == "Find safe room/shelter, shield yourself from debris"


def test_get_advice_underground_shelter():
    t1 = Tornado("testTornado", 113)
    t2 = Tornado("testTornado", 158)
    t3 = Tornado("testTornado", 206)
    t4 = Tornado("testTornado", 261)
    assert t1.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"
    assert t2.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"
    assert t3.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"
    assert t4.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"


def test_get_advice_no_need():
    t1 = Tornado("testTornado", 0)
    assert t1.get_advice() == "There is no need to panic"
