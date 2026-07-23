#lcm
def lcm(num1,num2):
    if num1>num2:
        num=num2
    else:
        num=num1
    lcm=1
    for i in range (1,num+1):
        if num1%i==0 and num2%i==0:
            num1=num1//i
            num2=num2//i
            lcm*=i
    lcm=lcm*num1*num2
    print("lcm : ",lcm)

lcm(5,6)
lcm(7,49)
# second method
def lcm2(num3,num4):
    num1=num3
    num2=num4
    while num2!=0:
        num1,num2=num2,num1%num2
    lcm=num3*num4//num1   
    print("lcm :",lcm)

lcm2(5,6)
lcm2(7,49)