from app import set_prices

def test_set_prices_sorting_works():
    #
    prices = [10, 30, 20]
    result_sorted = prices.sort()

    #
    result = set_prices(prices, 1.0)

    #
    assert result_sorted == result
    assert result_sorted == [10, 20, 30]


def test_set_prices_multiplying_works():
    #
    prices = [10, 30, 20]
    a = 2
    expected = [20, 40, 60]

    #
    result = set_prices(prices, a)

    #
    assert expected == result

def test_set_prices_multiplying_works_with_3():
    #
    prices = [10, 30, 20]
    a = 3
    expected = [30, 60, 90]

    #
    result = set_prices(prices, a)

    #
    assert expected == result
