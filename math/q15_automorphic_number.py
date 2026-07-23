#automorphic number
def length(number):
    count=0
    while number>0:
        rem=number%10
        number=number//10
        count+=1
    return count
def isautomorphic(number):
    num=number**2
    new_num=0
    n_digit=length(number)
    for i in range(n_digit):
        rem=num%10
        num=num//10
        new_num=new_num*10+rem
    if new_num==number:
        print(f"{number} is automorphic")

isautomorphic(5)
isautomorphic(6)
isautomorphic(9)
isautomorphic(25)

    