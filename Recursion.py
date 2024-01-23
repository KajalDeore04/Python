# factorial(5) = 5*4*3*2*1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

''' Uses recursion as it has self function called inside function'''

'''fib(0) = 0
fib(1) = 0 + 1
fib(n) = f(n-1) + f(n-2)'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(5):
    print(fibonacci(i))
