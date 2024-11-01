###############################
# LIST COMPREHENSION EXAMPLES #
###############################


# base list
numbers = [1, 2, 3, 4, 5, 6]
ms = [42, 666]

"""
This is basic list comprehension, it is simply iterating by each element of `numbers` and return it
as-is into the `result` list.
"""
result = [number for number in numbers]


"""
List comprehension wit the `if` statement, only those elements which pass by the condition 
`number > 3` will be present in the `result` list.
"""
result = [number for number in numbers if number > 3]

"""
Dict can be created using comprehension as well. Below example will create a dict with keys from
`numbers` list and each key having "duppa" value set. Please note each key in the dict **must** be
unique, otherwise code will result in undefined behaviour.
"""
dict_comprehend = {number: "duppa" for number in numbers}

"""
List comprehension with two `for` loops, this is not recomended, as it is hard to read, even harder
to debug and the product of such comprehension can be achieved faster (check `itertools` module).
"""
names = ["ukasz", "michal"]
surnames = ["kmicic", "wolodyjowski"]
result = [name + "_" + surname for name in names for surname in surnames]

"""
List comprehension with different `if` statement. This operation will have only event numbers in it.
"""
evens = [number for number in numbers if number % 2 == 0]


##############
# ASSIGMENTS #
##############

"""
a) using `numbers` list write list comprehension which will float version of each number.

result should look like this: `[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]`
"""
float_numbers = [float(number) for number in numbers]
print(float_numbers)

"""
b) using `numbers` list write dict comprehension which will have key being each number multiplied by
3 and each value being number multiplied by 5


result should look like this: `{3:5, 6:10, 9:15, 12:20, 15:25, 18:30}`
"""
numbers_dict = {number * 3: number * 5 for number in numbers}
print(numbers_dict)

"""
c) using `numbers` list write list comprehension which will have the same numbers but in the reverse
order

result should look like this: `[6, 5, 4, 3, 2, 1]`
"""
unocard_numbers = [number for number in reversed(numbers)]
print(unocard_numbers)