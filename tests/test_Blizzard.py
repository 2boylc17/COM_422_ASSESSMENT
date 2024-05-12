import pytest
from Blizzard import Blizzard
from Storm import Storm


def test_calculate_blizzard():
    s1 = Storm("test", 100)
    assert s1.name == "test"
