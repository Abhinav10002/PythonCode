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

'''def factorial(n):
    if n == 0:    # base case
        return 1
    
    return n * factorial(n-1)   # recursive case
print(factorial(10))

# Recursive stack

def fun(n):
    if n == 0:
        return 
    
    fun(n-1)
    print(n,end=" ")
fun(10)'''

# Fibonacci using Recursion
def fibonacci_number(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_number(n-1) + fibonacci_number(n-2)
print(fibonacci_number(34))
