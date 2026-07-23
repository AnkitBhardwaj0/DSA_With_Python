#check no is armstrong Number
number=int(input("enter a number"))
print(f"chek the {number} is armstrong ! ")
num=number
new_num=0
while num>0:
    rem=num%10
    num=num//10
    new_num+=rem**3
if number==new_num:
    print(f"{number} is armstrong")
else:
    print(f"{number} is not armstrong")