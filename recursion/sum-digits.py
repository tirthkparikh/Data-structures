def sum_digits(n):
    if n <= 0:
        return 0
    else:
        ans = n % 10 + sum_digits(n // 10)
    return ans


print(sum_digits(5102))
