# for loop vs Recursion

# Print 1 to n using loop
n = 5
i = 1
while i<=n:
    print(i)
    i += 1


# Print 1 to n using Recursion
def printNumbers(i,n):
    # base case
    if i > n:
        return
    
    # recursive case
    print(i,end=" ")
    printNumbers(i+1,n)

printNumbers(1,5)