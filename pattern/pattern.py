#pattern
"""
1. square starpattern
****
****
****
****
"""
def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()#for new line
"""
2. increasing right triangle starpattern
*
**
***
****
*****
"""
def right_tri(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()#for new line
"""
3. Hollow Square Pattern
*****
*   *
*   *
*   *
*****
"""
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()# for new line
"""
4. Inverted Right Triangle Pattern
*****
****
***
**
*
"""
def inverted_tri(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()# for new line
"""
5. Number Triangle
1
12
123
1234
12345
"""
def num_tri(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()# for new line
"""
6. Repeated Number Triangle
1
22
333
4444
55555
"""
def repeated_num_tri(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=" ")
        print()# for new line
"""
7. Alphabet Triangle
A
AB
ABC
ABCD
ABCDE
"""
def alphabet_tri(n):
    for i in range(n):
        for j in range(i+1):
            print(chr (65+j),end=" ")
        print()# for new line
"""
8. Repeated Alphabet Triangle
A
BB
CCC
DDDD
EEEEE
"""
def repeated_alphabet_tri(n):
    for i in range(n):
        for j in range(i+1):
            print(chr (65+i),end=" ")
        print()# for new line
"""
9. star pyramid
    *
   ***
  *****
 *******
*********
"""
def star_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        for j in range(n-i-1):
            print(" ",end=" ")
        print()# for new line
"""
10. Inverted Star Pyramid
*********
 *******
  *****
   ***
    *
"""
def inverted_star_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*(n-i)-1):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        print()# for new line

"""
11. diamond pattern
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""
def symmetry_pattern(n):
    star_pyramid(n)
    inverted_star_pyramid(n)
