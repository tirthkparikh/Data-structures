# 2 ways but first way has pass by ref issue so just use below mehod
row=3
col=4

arr=[[0 for i in range(col)] for j in range(row)]
arr[0][0]=1
print(arr)