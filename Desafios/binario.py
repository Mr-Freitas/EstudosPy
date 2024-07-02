def power(n):
    if n & (n-1) == 0:
        return True
    return False


print(power(512))