# https://lazzzaro.github.io/2020/05/06/crypto-RSA/#%E5%85%89%E6%BB%91%E6%95%B0

from gmpy2 import *
a = 2
k = 2
N = 
while True:
    a = powmod(a, k, N)
    res = gcd(a-1, N)
    if res != 1 and res != N:
        q = N // res
        print("p =",res)
        print("q =",q)
        break
    k += 1
