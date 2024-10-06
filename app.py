import time


def run_app(prices):

    # very important things
    time.sleep(60.00)

    print(prices)


def set_prices(prices, a):
    prices = [p * a for p in prices]

    prices.sort()
    return prices


def app():
    prices = [10, 30, 20]
    prices_sorted = set_prices(prices, 2.0)

    run_app(prices_sorted)


app()
