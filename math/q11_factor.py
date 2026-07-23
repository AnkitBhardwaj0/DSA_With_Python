#factor
def factor(num):
    fact=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            fact.append(i)
            if num//i not in fact:
                fact.append(num//i)
    return fact

print(sorted(factor(25)))
print(sorted(factor(36)))