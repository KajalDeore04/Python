x = 4  # global variable
print(x)  # 4


def function():
    x = 5  # local var can only be accessed through function
    y = 1  # local var
    print(f"Local x is {x}")  # 5


print(f"Global x is {x}")  # 4
function()

x = 5  # overwriting x variable
print(f"Global x is {x}")  # 5
# print(y) # (error) local var hence cannot be accessed outside
