# Input Format: N = 3
# Result:
# 1
# 2 3
# 4 5 6

# Input Format: N = 6
# Result:
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 16  17  18  19  20  21
n = int(input("enter your number: "))
k = 1
for i in range(n):
    for j in range(i + 1):
        print(k, end=" ")
        k += 1
    print()
