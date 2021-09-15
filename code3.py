def recurv(n):
    if n<=1:
        return n
    else:
        return n + recurv(n-1)
        
if num < 0:
    print("print +ve number")
else:
    print("sum is",recurv(num))


