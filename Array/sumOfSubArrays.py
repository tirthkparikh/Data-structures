
"""
Below methodis subarray sum by cary forward also can be done by 3 for loop in bruteforce(the way we print all subarray's)
"""

a=[2,5,3]
ans=0
for i in range(0,len(a)):
    total=0
    for j in range(i,len(a)):
        total+=a[j]    
        ans=ans+total   

print(ans)


"""Now the contribution tech  
We will calcutae how many time a[i] comes in total 
2->3
5->4
3->3

how to calculate ?
let us suppoe we calcute for 5
possible start index [0,1] and it's length is 2
possible of end index[1,2] ans it's length is 2
total = 2*2
so we can can see that start index is from 0 to i=(i+1)
and end index are from i to len(a)-1= (n-i)
"""

ans=0
for i in range(0,len(a)):
    ans=ans + a[i]*((i+1)*(len(a)-i))
print(ans)    
