#Harshad (Niven) Number
def sum_of_digit(number):
    sum=0
    while number>0:
        rem=number%10
        number=number//10
        sum+=rem
    return sum

def iSharshed(number):
    sum=sum_of_digit(number)
    if number%sum==0:
        print(f"{number} is harshed number")

iSharshed(18)
iSharshed(2)
iSharshed(3)
iSharshed(11)
