# for loop vs Recursion

# Print 1 to n using loop
'''n = 5
i = 1
while i<=n:
    print(i)
    i += 1


# Print 1 to n using Recursion
def printNumbers(i,n):
    if i > n:
        return
    
    print(i,end=" ")
    printNumbers(i+1,n)
printNumbers(1,10)'''

# Factorial of a number using Recursion

def factorial(n):
    if n == 0:    # base case
        return 1
    
    return n * factorial(n-1)   # recursive case
print(factorial(10))
