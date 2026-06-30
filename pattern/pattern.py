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
"""
"""
"""
16. Floyd's Triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
"""
17. Alphabet Increment Triangle
A
BC
DEF
GHIJ
KLMNO
"""
"""
18. Reverse Alphabet Triangle
E
DE
CDE
BCDE
ABCDE
"""
"""
19.Alphabet Palindrome Pyramid
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""
"""
20. Increasing Number Triangle
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
"""
Reverse Number Triangle
5
54
543
5432
54321
"""
"""
22. Palindrome Number Pyramid
1
121
12321
1234321
123454321
"""
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
"""
26. Hollow Pyramid
    *
   * *
  *   *
 *     *
*********
"""
"""
27.Rhombus Pattern
    *****
   *****
  *****
 *****
*****
"""
"""
28. Hollow Rhombus
    *****
   *   *
  *   *
 *   *
*****
"""
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
