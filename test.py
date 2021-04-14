def oops():
    try:
        return 1
    finally:
        return 2
k = oops()
print(k)