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
'''def fibonacci_number(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_number(n-1) + fibonacci_number(n-2)
print(fibonacci_number(34))
'''

# LISTS in Python

'''list1 = ["Abhinav","Aman","Ravi","Rahul"]
list1[0] = "Dipanshu"
print(list1[0])
print(list1[2])
print(list1[-1])
print(len(list1))'''

'''list2 = ["Abhinav",5,9.87,True,2344]
print(list2)'''

# Operations on list
'''list3 = [34,65,67,37,90,100]
list3.append(1001)
list3.append([567,988,5678,4])
list3.extend([567,988,5678,4])
print(list3[7][2])'''

'''list4 = [34,65,67,37,90,100]
list4.insert(3,100)
print(list4)
'''

'''list4 = [34,65,67,37,90,100]
list4.remove(67)
list4.pop(1) # by default removes last element
print(list4)

list4.clear()  # deletes the whole list
print(list4)'''

