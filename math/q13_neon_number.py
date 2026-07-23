#check neon number
def square(number):
    return number**2
def isneon_number(number):
    sq=square(number)
    sum=0
    while sq>0:
        rem=sq%10
        sq=sq//10
        sum+=rem
    if sum==number:
        print(f"{number } is neon number")
    else:
        print(f"{number } is not neon number")
isneon_number(9)
isneon_number(12)
isneon_number(1)

    