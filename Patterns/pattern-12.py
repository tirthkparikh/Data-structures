"""
Input Format: N = 3
Result: 
1    1
12  21
123321

Input Format: N = 6
Result:   
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
"""
n = int(input("enter your number: "))
for i in range(0, n):
    for j in range(i + 1):
        print(j + 1, end="")
    for k in range(2 * (n - 1), 2 * i, -1):
        print(" ", end="")
    for j in range(i + 1, 0, -1):
        print(j, end="")
    print()
