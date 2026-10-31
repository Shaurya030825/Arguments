x= int(input("Pleae enter the value: "))
def factorial(x):
    """This is a reursive function to find the factorial of an integer"""
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial.__doc__)
print("The factorial of x:", factorial(x))