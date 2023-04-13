import gmpy2
import random


def divide_pq(e, d, n):
    k = e*d - 1
    while True:
        g = random.randint(2, n-1)
        t = k
        while True:
            if t % 2 != 0:
                break
            t //= 2
            x = pow(g, t, n)
            if x > 1 and gmpy2.gcd(x-1, n) > 1:
                p = gmpy2.gcd(x-1, n)
                return (p, n//p)


e = 
d = 
n = 

p,q = divide_pq(e, d, n)
print(f'p = {p}')
print(f'q = {q}')
