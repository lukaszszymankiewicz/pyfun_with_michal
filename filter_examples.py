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


################
# MAP EXAMPLES #
################


def mulitply_by_three(number):
    return number * 3


result = map(mulitply_by_three, numbers)

################
# ZIP EXAMPLES #
################

numbers = [1, 2, 3, 4, 5, 6]
letters = ["a", "b", "c", "d", "e", "f"]

result = dict(zip(letters, numbers))


##############
# ASSIGMENTS #
##############


new_numbers = [0.0, 1, 1.0, 2, "a", 3]

"""
a) using `new_numbers` list write filter to filter **out** every string and
float number saving only integers there

result should look like this: `[1, 2, 3]`
"""

new_letters = ["a", "b", "c"]
"""
b) using `new_numbers` list write map to change letters to big ones

result should look like this: `["A", "B", "C"]`
"""

earns = [100, 200, 300]
costs = [50, 100, 200]

"""
c) using `earns` and `costs` lists write for loop using `zip` to calculate
profit for each value present.

Profit is money earned minus costs (earn - cost)

result should look like this: `[50, 100, 100]`
"""

"""
hint try to use such loop:

for (...) in zip(earns, costs):
    (...)
"""
