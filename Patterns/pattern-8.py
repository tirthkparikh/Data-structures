"""
Input Format: N = 3
Result: 
*****  
 ***
  *   
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
"""

n = int(input("enter the number: "))
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        print(" ", end="")
    for k in range(2 * i + 1, 0, -1):
        print("*", end="")
    print()
