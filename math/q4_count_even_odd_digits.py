#count even odd digits
num=int(input("enter a number"))
print(f"number : {num}  ")
while num>0:
    rem=num%10
    num=num//10
    if rem%2==0:
        print(f"{rem} is even")
    else:
        print(f"{rem} is odd")