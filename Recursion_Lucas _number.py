def P(n):
    if n == 0:
        return n
    elif n < 0:
        return -1
    return 5*(P(n-1))+1

test = P(4)
print(test)