#reverse a Number
num=int(input("enter a number"))
print(f"reverse the {num} ")
rev_num=0
while num>0:
    rem=num%10
    num=num//10
    rev_num=rev_num*10+rem
print(f"reverse number is : {rev_num}")
