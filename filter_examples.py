###################
# FILTER EXAMPLES #
###################


numbers = [1, 2, 3, 4, 5, 6]


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


result = list(filter(is_even, numbers))
# print(result)


################
# MAP EXAMPLES #
################


def mulitply_by_three(number):
    return number * 3


result = map(mulitply_by_three, numbers)

# print(next(result))


################
# ZIP EXAMPLES #
################

numbers = [1, 2, 3, 4, 5, 6]
letters = ["a", "b", "c", "d", "e", "f"]

result = dict(zip(letters, numbers))

print(result)
