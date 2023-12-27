def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))


def printfib(n):
    if n == 0:
        return 0
    if n == 1:
        return [0, 1]
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[0] = 0
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr


print(printfib(6))
