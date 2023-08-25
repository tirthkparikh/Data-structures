a=[[1,2,3],[2,4,5,5]]
for i in a:
    for j in i:
        print(j,end=" ")
    print()


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()