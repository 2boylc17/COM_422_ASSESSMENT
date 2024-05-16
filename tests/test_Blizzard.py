import pytest
from Blizzard import Blizzard
from Storm import Storm


def test_create_blizzard():
    b1 = Blizzard("testBlizzard", 100, 10)
    assert b1.name == "testBlizzard" and b1.wind_speed == 100 and b1.temp == 10


def test_classify_blizzard_blizzard():
    b1 = Blizzard("testBlizzard", 35, 10)
    b2 = Blizzard("testBlizzard", 36, 10)
    assert b1.calculate_classification() == "Blizzard"
    assert b2.calculate_classification() == "Blizzard"


def test_classify_blizzard_severe_blizzard():
    b1 = Blizzard("testBlizzard", 45, -12)
    b2 = Blizzard("testBlizzard", 46, -12)
    b3 = Blizzard("testBlizzard", 45, -13)
    b4 = Blizzard("testBlizzard", 46, -13)
    assert b1.calculate_classification() == "Severe Blizzard"
    assert b2.calculate_classification() == "Severe Blizzard"
    assert b3.calculate_classification() == "Severe Blizzard"
    assert b4.calculate_classification() == "Severe Blizzard"


def test_classify_blizzard_snow_storm():
    b1 = Blizzard("testBlizzard", 34, 20)
    b2 = Blizzard("testBlizzard", 34, -20)
    assert b1.calculate_classification() == "Snow Storm"
    assert b2.calculate_classification() == "Snow Storm"


def test_get_advice_essential_travel():
    b1 = Blizzard("testBlizzard", 40, 10)
    assert b1.get_advice() == "Keep warm, Do not travel unless absolutely essential."


def test_get_advice_avoid_travel():
    b1 = Blizzard("testBlizzard", 50, -20)
    assert b1.get_advice() == "Keep warm, avoid all travel."


def test_get_advice_take_care():
    b1 = Blizzard("testBlizzard", 0, 10)
    assert b1.get_advice() == "Take care and avoid travel if possible."
