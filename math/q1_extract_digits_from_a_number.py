#Extract Digits from a Number and count digit
num=int(input("enter a number"))
print(f"Extracted digit from {num} : ",end=" ")
count=0
while num>0:
    rem=num%10
    num=num//10
    count+=1
    print(rem,end=",")
print("\n",count," digit number")
