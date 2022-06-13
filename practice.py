#1. Write a Python Program to Find the Factorial of a Number?
def fact(x):
    if x >= 0:
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return x*fact(x-1)
print(fact(5))