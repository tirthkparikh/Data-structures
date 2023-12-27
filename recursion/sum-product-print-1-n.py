def prod(n):
    if type(n)!=int or n<0:
        return "error"
    if n==1:
        return 1
    else:
        return n*prod(n-1)
def sum(n):
    if type(n)!=int or n<0:
        return "error"
    if n==1:
        return 1
    else:
        return n+sum(n-1)
def prin(n):
    if type(n)!=int or n<0:
        return "error"
    if n==1:
        return 1
    else:
        print(n)
        return prin(n-1)
    
print(prod(5))
print(sum(5))
print(prin(5))