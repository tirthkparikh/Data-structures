#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        import math
        if N < 0:
            return 0
        
        # Using logarithmic property to find the number of digits
        if N <= 1:
            return 1
        
        digits = 0
        for i in range(2, N + 1):
            digits += math.log10(i)
        
        return math.floor(digits) + 1

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends