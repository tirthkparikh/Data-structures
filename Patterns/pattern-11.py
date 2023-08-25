"""
Input Format: N = 3
Result: 
1
01
101

Input Format: N = 6
Result:   
1
01
101
0101
10101
010101
"""

n = int(input("enter the number: "))
x = 0
for i in range(0, n):
    if i % 2 == 0:
        x = 1
    else:
        x = 0
    for j in range(0, i + 1):
        print(x, end="")
        if x == 1:
            x = 0
        else:
            x = 1
    print()
