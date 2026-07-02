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
11. Symmetry pattern
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
"""
12. Diamond Pattern
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
def diamond_pattern(n):
    stars=2*n-1
    for i in range(2*n-1):
        if  i<n:
            for j in range(n-i-1):
                print(" ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            for j in range(n-i-1):
                print(" ",end=" ")
        else:
            stars -=2
            for j in range(i-n+1):
                print(" ",end=" ")
            for j in range(stars):
                print("*",end=" ")

            for j in range(i-n+1):
                print(" ",end=" ")
        print()# for new line
#method two for diamond pattern
def diamond(n):
    for i in range(2*n-1):
        distance=abs(n-i-1)
        spaces=distance
        stars=2*(n-distance)-1
        for _ in range(spaces):
            print(" ",end=" ")
        for _ in range(stars):
            print("*",end=" ")
        print()# for new line
"""
13. Half Diamond Star Pattern
*
**
***
****
*****
****
***
**
*
"""
def half_diamond(n):
    for i in range(1,2*n):
        if i >n:
            stars=2*n-i
            print("*"*stars)
        else:
            print("*"*i)

"""
14. Butterfly Pattern
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""
def butterfly_pattern(n):
    for i in range(1,2*n):
        if i<=n:
            for _ in range (i):
                print("*",end=" ")
            for _ in range (2*(n-i)):
                print(" ",end=" ")
            for _ in range (i):
                print("*",end=" ")
        else:
            for _ in range (2*n-i):
                print("*",end=" ")
            for _ in range (2*(i-n)):
                print(" ",end=" ")
            for _ in range (2*n-i):
                print("*",end=" ")

        print()
# Method 2: Optimized solution (avoids duplicate printing code)
def butterfly(n):
    for i in range(1,2*n):
        if i <= n:
            stars = i
            spaces = 2 * (n - i)
        else:
            stars = 2 * n - i
            spaces = 2 * (i - n)

        for _ in range(stars):
            print("*", end=" ")
        for _ in range(spaces):
            print(" ", end=" ")
        for _ in range(stars):
            print("*", end=" ")
        print()
""" 
15.  Binary Triangle Pattern
1
01
101
0101
10101
"""
def binary_triangle(n):
    for i in range(n):
        if i%2==0:
            start=1
        else:
            start=0
        for _ in range(i+1):
            print(start,end=" ")
            start=1-start
        print()#for new line

"""
16. Floyd's Triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
def floyds_triangle(n):
    num=1
    for i in range(n):
        for _ in range(i+1):
            print(num,end=" ")
            num+=1
        print()#for new line  
"""
17. Alphabet Increment Triangle
A
BC
DEF
GHIJ
KLMNO
"""
def alphabet_increment_triangle(n):
    num=65
    for i in range(n):
        for _ in range(i+1):
            print(chr(num),end=" ")
            num+=1
        print()#for new line
#another method for alphabet increment triangle
def alphabet_increment_tri(n):
    ch = 'A'
    for i in range(n):
        for _ in range(i + 1):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)
        print()
"""
18. Reverse Alphabet Triangle
E
DE
CDE
BCDE
ABCDE
"""
def reverse_alphabet_triangle(n):
    for i in range(n):
        start=chr(ord('A')+n-i-1)
        for _ in range(i+1):
            print(start,end=" ")
            start=chr(ord(start)+1)
        print()#for new line

"""
19.Alphabet Palindrome Pyramid
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""
def alphabet_palindrome_pyramid(n):
    for i in range(n):
        spaces=n-i-1
        for _ in range(spaces):
            print(" ",end=" ")
        for _ in range(2*i+1):
            if _ <= i:
                print(chr(ord('A')+_),end=" ")
            else:
                print(chr(ord('A')+2*i-_),end=" ")
        print()#for new line
# another method for alphabet palindrome pyramid
def alphabet_palindrome_pyramid_2(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end=" ")
        ch = ord('A')
        for _ in range(2 * i + 1):
            print(chr(ch), end=" ")
            if _ < i:
                ch += 1
            else:
                ch -= 1
        print()#for new line
"""
20. Increasing Number Triangle
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
def increasing_number_triangle(n):
    for i in range(n):
        start=i+1
        for _ in range(n-i):
            print(start+_,end=" ")
        print()#for new line 
"""
Reverse Number Triangle
5
54
543
5432
54321
"""
def reverse_number_triangle(n):
    for i in range(n):
        for _ in range(i+1):
            print(n-_,end=" ")
        print()
"""
22. Palindrome Number Pyramid
1
121
12321
1234321
123454321
"""
def palindrome_number_pyramid(n):
    for i in range(n):
        num=0
        for j in range(2*i+1):
            if j <= i:
                num+=1
            else:
                num-=1
            print(num,end=" ")
        print()
"""
23. Concentric Number Square
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""
def concentric_number_square(n):
    size=2*n-1
    for i in range(size):
        for j in range (size):
            min_dist=min(i,j,size-1-i,size-1-j)
            print(n-min_dist,end=" ")
        print()
#another method for concentric numbe square
def concentric_number_square_2(n):
    size=2*n-1
    for i in range(size):
        for j in range (size):
            max_dist=max(abs(n-1-i),abs(n-1-j))
            print(max_dist+1,end=" ")
        print()
"""
24. Hollow Butterfly
*        *
**      **
* *    * *
*  *  *  *
*   **   *
*  *  *  *
* *    * *
**      **
*        *
"""
def hollow_butterfly(n):
    for i in range (1,2*n):
        if i<=n:
            stars=i
            spaces=2*(n-i)
        else:
            stars=2*n-i
            spaces=2*(i-n)
        for j in range(stars):
            if j==0 or j==stars-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        for _ in range(spaces):
            print(" ",end=" ")
        for j in range(stars):
            if j==0 or j==stars-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
# improve code for hollow butterfly pattern 
def hollow_wing(stars):
    for j in range(stars):
        if j == 0 or j == stars - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
###
def pattern_improve_hollow_butterfly(n):
    for i in range (1,2*n):
        if i<=n:
            stars=i
            spaces=2*(n-i)
        else:
            stars=2*n-i
            spaces=2*(i-n)
        hollow_wing(stars)
        for _ in range(spaces):
            print(" ",end=" ")
        hollow_wing(stars)
        print()  

"""
25.Hollow Diamond 
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""

def hollow_diamond(n):
    for i in range(1,2*n):
        if i<=n:
            stars=2*i-1
            spaces=n-i
        else:
            stars=2*(2*n-i)-1
            spaces=i-n
            spaces+=1
        for _ in range (spaces):
            print(" ",end=" ")
        for j in range(stars):
            if j==0 or j==stars-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

"""
26. Hollow Pyramid
    *
   * *
  *   *
 *     *
*********
"""
def hollow_pyramid(n):
    for i in range(1,n+1):
        stars=2*i-1
        spaces=n-i
        for _ in range (spaces):
            print(" ",end=" ")
        for j in range(stars):
            if j==0 or j==stars-1 or i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
"""
27.Rhombus Pattern
    *****
   *****
  *****
 *****
*****
"""
def rhombus(n):
    for i in range (1,n+1):
        for _ in range(n-i):
            print(" ",end=" ")
        for _ in range (n):
            print("*",end=" ")
        print()
"""
28. Hollow Rhombus
    *****
   *   *
  *   *
 *   *
*****
"""
def hollow_rhombus(n):
    for i in range (1,n+1):
        for _ in range(n-i):
            print(" ",end=" ")
        for j in range (n):
            if i==1 or i==n or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
"""
29. X Pattern
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *

"""
def x_pattern(n):
    for i in range(1,2*n):
        if i<=n:
            stars=2*(n-i)+1
            spaces=i-1
        else:
            stars=2*(i-n)+1
            spaces=2*n-i-1
        for _ in range (spaces):
            print(" ",end=" ")
        for j in range(stars):
            if j==0 or j==stars-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
"""
30.Hourglass Pattern
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""
def hourglass(n):
    for i in range(1,2*n):
        if i<=n:
            stars=2*(n-i)+1
            spaces=i-1
        else:
            stars=2*(i-n)+1
            spaces=2*n-i-1
        for _ in range (spaces):
            print(" ",end=" ")
        for j in range(stars):
            print("*",end=" ")
            
        print()
"""
31.Heart Pattern ❤️
 **   **
**** ****
*********
 ********
  ******
   ****
    **

"""
def heart_pattern(n):#n=4
    spaces=n-1
    for i in range(1,2*n):
        if i<n-1:
            stars=2*i
            for j in range(stars):
                if j==0 and i==1:
                    print(" ",end=" ")
                print("*",end=" ")
            for _ in range(spaces):
                print(" ",end=" ")
            spaces-=2
            
            for j in range(stars):
                print("*",end=" ")
        elif i==n-1:
            for j in range(2*n+1):
                print("*",end=" ")
            spaces+=2
            stars=2*n
        else:
            for j in range(spaces):
                print(" ",end=" ")
                
            for j in range(stars):
                print("*",end=" ")
            spaces+=1
            stars-=2
        print()


    
