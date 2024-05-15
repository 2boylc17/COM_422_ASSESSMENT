import pytest
from Blizzard import Blizzard
from Storm import Storm


def test_create_blizzard():
    b1 = Blizzard("testblizzard", 100, 40)
    assert b1.name == "testblizzard" and b1.wind_speed == 100 and b1.temp == 40
