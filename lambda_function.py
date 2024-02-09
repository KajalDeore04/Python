# like a single expression

def double(x):
    return x * 2


double = lambda x: x * 2  # shortened function
# both the function are same but to lower the lines

cube = lambda x: x * x * x

avg = lambda x, y: (x + y) / 2
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(4))
print(avg(2, 45, 6))


def appl(fx, value):
    return 6 + fx(value)


print(appl(cube, 2))  # function in function
print(appl(lambda x: x * x * x, 2))  # works same
