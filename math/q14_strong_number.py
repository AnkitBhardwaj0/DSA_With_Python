#strong number
def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
def isstrong_number(number):
    sum=0
    num=number
    while num>0:
        rem=num%10
        num=num//10
        fact=factorial(rem)
        sum+=fact
    if sum==number:
        print(f"{number } is strong number")

    
isstrong_number(145)
for i in range(1,150):
    isstrong_number(i)