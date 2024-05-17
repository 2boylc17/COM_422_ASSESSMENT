from Hurricane import Hurricane


def test_create_hurricane():
    h1 = Hurricane("testhurricane", 100)
    assert h1.name == "testhurricane" and h1.wind_speed == 100


def test_classify_hurricane_category_1():
    h1 = Hurricane("testhurricane", 74)
    h2 = Hurricane("testhurricane", 80)
    h3 = Hurricane("testhurricane", 95)
    assert h1.calculate_classification() == "Category one"
    assert h2.calculate_classification() == "Category one"
    assert h3.calculate_classification() == "Category one"


def test_classify_hurricane_category_2():
    h1 = Hurricane("testhurricane", 96)
    h2 = Hurricane("testhurricane", 100)
    h3 = Hurricane("testhurricane", 110)
    assert h1.calculate_classification() == "Category two"
    assert h2.calculate_classification() == "Category two"
    assert h3.calculate_classification() == "Category two"


def test_classify_hurricane_category_3():
    h1 = Hurricane("testhurricane", 111)
    h2 = Hurricane("testhurricane", 120)
    h3 = Hurricane("testhurricane", 129)
    assert h1.calculate_classification() == "Category three"
    assert h2.calculate_classification() == "Category three"
    assert h3.calculate_classification() == "Category three"


def test_classify_hurricane_category_4():
    h1 = Hurricane("testhurricane", 130)
    h2 = Hurricane("testhurricane", 140)
    h3 = Hurricane("testhurricane", 156)
    assert h1.calculate_classification() == "Category four"
    assert h2.calculate_classification() == "Category four"
    assert h3.calculate_classification() == "Category four"


def test_classify_hurricane_category_5():
    h1 = Hurricane("testhurricane", 157)
    h2 = Hurricane("testhurricane", 9999)
    assert h1.calculate_classification() == "Category five"
    assert h2.calculate_classification() == "Category five"


def test_classify_hurricane_tropical_storm():
    h1 = Hurricane("testhurricane", 73)
    assert h1.calculate_classification() == "Tropical Storm"


def test_get_advice_close_shutters():
    h1 = Hurricane("testhurricane", 73)
    h2 = Hurricane("testhurricane", 80)
    h3 = Hurricane("testhurricane", 100)
    assert h1.get_advice() == "Close storm shutters and stay away from windows"
    assert h2.get_advice() == "Close storm shutters and stay away from windows"
    assert h3.get_advice() == "Close storm shutters and stay away from windows"


def test_get_advice_coastal_regions():
    h1 = Hurricane("testhurricane", 120)
    assert h1.get_advice() == "Coastal regions are encouraged to evacuate"


def test_get_advice_evacuate():
    h1 = Hurricane("testhurricane", 170)
    assert h1.get_advice() == "Evacuate"
