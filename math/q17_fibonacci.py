#fibonacci
def fibonacci(number):
    a=0
    b=1
    for i in range(number):
        print(a, end=" ")
        a,b=b,b+a
    print("\n")

fibonacci(1)
fibonacci(2)
fibonacci(5)
fibonacci(10)