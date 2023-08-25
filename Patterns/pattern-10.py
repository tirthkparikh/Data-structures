"""
Input Format: N = 3
Result: 
  *  
  **
  ***  
  **
  *   
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
"""

n = int(input("enter the number: "))

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()
