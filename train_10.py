def fun(n):
    if n > 100:
        print(n)
        return n - 5
    print(n)
    return fun(fun(n + 11))


print(fun(45))
