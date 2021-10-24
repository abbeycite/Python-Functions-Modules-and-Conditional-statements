def rFib(n):
    if n == 0:
        return 0
    elif n == 11 or n == 2:
        return 1
    return rFib(n-1)+rFib(n-2)
