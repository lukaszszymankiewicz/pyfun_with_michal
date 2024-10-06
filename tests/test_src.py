from app import set_prices
from app import app

def test_set_prices_sorting_works():
    #
    prices = [10, 30, 20]
    prices.sort()

    #
    result = set_prices(prices, 1.0)

    assert prices == result
    assert prices == [10, 20, 30]


def test_set_prices_multiplying_works():
    prices = [10, 20, 30]
    a = 2
    # Obliczenie wyniku
    expected_result = [p * a for p in prices]

    # Wywołanie funkcji
    result = set_prices(prices, a)

    # Sprawdzenie
    assert result == expected_result


