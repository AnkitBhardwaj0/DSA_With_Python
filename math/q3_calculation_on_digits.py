#sum,products of Digits ,smaller digits,larger digits 
num=int(input("enter a number"))
print(f"number : {num}  ")
sum=0
product=1
smaller=9
larger=0
while num>0:
    rem=num%10
    num=num//10
    sum+=rem
    product*=rem
    if smaller>rem:
        smaller=rem
    if larger<rem:
        larger=rem
print(f"sum of digits : {sum}")
print(f"product of digits : {product}")
print(f"smaller digits : {smaller}")
print(f"larger digits : {larger}")
