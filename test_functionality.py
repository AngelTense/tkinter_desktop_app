import math

def reduce_fraction(n, m):
    k = math.gcd(n, m)
    return (n//k, m//k)


print(reduce_fraction(3, 9))