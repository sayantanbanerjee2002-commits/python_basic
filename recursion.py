# factorial of a number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
num = int(input('Enter a number')) 
result = fact(num)
print(f"factorial of {num} is: {result}")