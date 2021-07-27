def fibn(n):
    """
    Returns nth number of fibanocci number
    
    Input: n positive integer
    
    Output: nth number of fibanocci number
    
    >>>fibn(6)
    8
    """
    return fibn(n-1)+fibn(n-2) if n>=3 else 1
b = fibn(4)
print(b)
