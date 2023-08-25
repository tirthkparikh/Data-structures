"""
******
**  **
*    *
*    *
**  **
******

Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
"""
n=6
for i in range(n):
    for j in range(n,i,-1):
        print("*",end="")
    for j in range(2,2*i+2):
        print(" ",end="")
    for j in range(n,i,-1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*(n-1),2*i,-1):
        print(" ",end="")    
    for j in range(i+1):
        print("*",end="")
    print()