#find armstrong Number
def armstrong(number):
    rev_num=0
    num=number
    while num>0:
        rem=num%10
        num=num//10
        rev_num+=rem**3
    if number==rev_num:
        print(f"{number} is palindrome")

for i in range(1,1000):
    armstrong(i)