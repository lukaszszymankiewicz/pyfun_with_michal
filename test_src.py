from app import set_prices
from app import app

def test_set_prices_sorting_works():
    #
    prices = [10, 30, 20]
    prices.sort()
   # return prices

    #
    result = set_prices(prices, 1.0)

    # TODO: correct me! MŁ:DONE, ale potrzebna konsultacja czy na pewno dobrze i dlaczego 50% na pierwszym teście. Update: Było 50% ze względu na return prices, dopytać dlaczego

    # if result_sorted != result:
    #     raise AssertionError()
    assert prices == result
    assert prices == [10, 20, 30] #Sprawdzic czy mogę dodać mnożnik by niezależnie od wartości pod a test był poprawny




def test_set_prices_multiplying_works(prices=[10, 20, 30], a=2):
    # TODO: write me! MŁ: Done, dlaczego nie mogę prices rozpisać niżej? Pycharm mi od razu tu przeniósł jak wczesniej byl błąd

    # Obliczenie wyniku
    expected_result = [p * a for p in prices]

    # Wywołanie funkcji
    result = set_prices(prices, a)

    # Sprawdzenie
    assert result == expected_result
