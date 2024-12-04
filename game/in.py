import time

player_input = None

while True:
    if player_input == "H" or player_input is None:
        player_input = input("\n P[ass] or H[it]?")

    # player would input only values "P" or "H"
    # TODO: validation, uppercase letters check

    print(player_input)
    print("~~~~~Game logic")

    time.sleep(0.5)