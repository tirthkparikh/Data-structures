def func(x, y):
    if y<1:
        return "power should be greater than one"
    if y == 0:
        return 1
    else:
        return x * func(x, y - 1)


print(func(5,0))
