# import math 
# n = 24
# print(int("24"))
# count = 1
# # to count facotor
# for i in range(1, int(n / 2)+1):
#     if n % i == 0:
#         count += 1
#         print(i)
# print(count)

# #to count mulitple factors

# l=[1,2,3,4,5]
# p1=1
# p2=3
# while p1<p2:
#     l[p1],l[p2]=l[p2],l[p1]
#     p1+=1
#     p2-=1
# print(l)
# print(l[:3])
# print(l[-2:-1:]+l[:len(l)-2:])
# for i in range(math.floor(len(l)/2)):
#     temp=l[i]
#     l[i]=l[len(l)-i-1]
#     l[len(l)-i-1]=temp
# print(l)



# class Main:
#     @staticmethod
#     def fun(arr):
#         arr[3] = 98
#         return

# if __name__ == "__main__":
#     arr = [10, 20, 30, 40, 50]
#     Main.fun(arr)
#     print(arr[3])


def solve(A):
        px_sum=0
        for i in range(len(A)):
            px_sum+=A[i]
        high_order=px_sum
        print(px_sum)
        low_order=0
        for i in range(len(A)):
            if i ==0:
                if low_order==high_order-A[i]:
                    return 0
                high_order-=A[0]
                low_order+=A[0]
            else:
                print(high_order,low_order,i)
                if high_order==low_order:
                    return i
                high_order-=A[i-1]
                low_order+=A[i-1]
        return -1
print(solve([-7, 1, 5, 2, -4, 3, 0]))