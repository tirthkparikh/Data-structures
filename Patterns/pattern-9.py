"""
Input Format: N = 3
Result: 
  *  
 ***
***** 
*****  
 ***
  *   
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
"""

n = int(input("enter the number: "))

for i in range(0, n):
    for j in range(i, n):
        print(" ", end="")
    for k in range(0, 2 * i + 1):
        print("*", end="")
    print()
for b in range(n - 1, -1, -1):
    for a in range(b, n):
        print(" ", end="")
    for c in range(2 * b + 1, 0, -1):
        print("*", end="")
    print()
