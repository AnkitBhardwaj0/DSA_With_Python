#perfect number
def factor(num):
    fact=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            fact.append(i)
            if num//i not in fact:
                fact.append(num//i)
    return fact

def isperfect_num(number):
    sum=0
    fact=sorted(factor(number))
    fact.pop()
    for i in fact:
        sum+=i
    if sum==number:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")

isperfect_num(6)
isperfect_num(9)
isperfect_num(36)
isperfect_num(28)
isperfect_num(496)
isperfect_num(8128)
isperfect_num(33550336)
