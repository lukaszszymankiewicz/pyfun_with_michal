import time


def run_app(prices):

    # very important things
    time.sleep(02.00)

    print(prices)


def set_prices(prices, a):
    prices = [p * a for p in prices]

    # Poniższe kod tworzył listę o wartościach none, poproszę o wyjasnienie czemu tak to działa
    # prices_sorted = prices.sort() poprawnie prices_sorted = sorted(prices)
    # return prices_sorted

    # Poprawione
    prices.sort()
    return prices


def app():
    prices = [10, 30, 20]
    prices_sorted = set_prices(prices, 2.0)

    run_app(prices_sorted)


app()
