'''num = int(input())
if num == 1:
    print("Not prime")
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")'''

lower = int(input())
upper = int(input())

for num in range(lower,upper + 1):
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                break
        else:
            print(num)
