#check no is palindrome Number
number=int(input("enter a number"))
print(f"chek the {number} is palindrome ! ")
num=number
rev_num=0
while num>0:
    rem=num%10
    num=num//10
    rev_num=rev_num*10+rem
if number==rev_num:
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")