from app import set_prices

def test_set_prices_sorting_works():
    #
    prices = [10, 30, 20]
    result_sorted = prices.sort()

    #
    result = set_prices(prices, 1.0)

    # TODO: correct me!

    # if result_sorted != result:
    #     raise AssertionError()
    assert result_sorted == result
    assert result_sorted == [10, 20, 30]


def test_set_prices_multiplying_works():
    # TODO: write me!

    assert True