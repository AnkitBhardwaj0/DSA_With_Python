def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num," is not prime") 
            break
    else:
            print(num," is prime")

isprime(37)
isprime(2)
isprime(3)
isprime(4)
isprime(6)
isprime(49)
isprime(25)
