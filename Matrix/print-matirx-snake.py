arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(len(arr)):
    if i%2==0:
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
    else:
        for j in range(len(arr[i])-1,-1,-1):
            print(arr[i][j],end=" ")
    