def cube(x):
    return x * x * x


print(cube(2))

elements = [1, 2, 5, 8, 3]
newL = []  # create new empty list
for item in elements:
    newL.append(cube(item))  # traverse each and replace that item with its cube
print(newL)  # prints new list

# but instead we can do ----

newL = list(map(cube, elements))  # need to be changed into desired datatype coz it returns map object
newL = list(map(lambda x: x * x * x, elements))
print(newL)


# ------------------------------------------------------------------------------
def filter_function(a):
    return a > 4


newnewl = list(filter(filter_function, elements))  # filters out elements
print(newnewl)

# ---------------------------------------------------------------------------------


from functools import reduce  # need to be imported

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)  # reduces the list by adding
print(sum)
