n=int(input('Enter a number: '))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
factorial(n)
#print("Enter a number:",n)
print("Factorial of",n,"is",factorial(n))