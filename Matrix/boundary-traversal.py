arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#  handeling corner case
# if row or col are just one we need to print them only
r=len(arr)
c=len(arr[0])
if r==1:
    for i in range(c):
        print(arr[0][i],end=" ")
elif c==1:
    for i in range(r):
        print(arr[i][0],end=" ")
else:
    for i in range(c):
        print(arr[0][i],end=" ")
    for i in range(1,r):
        print(arr[i][c-1],end=" ")
    for i in range(c-2,-1,-1):
        print(arr[r-1][i],end=" ")
    for i in range(r-2,0,-1):
        print(arr[i][0],end=" ")