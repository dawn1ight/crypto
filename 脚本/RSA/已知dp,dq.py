from gmpy2 import *

p = 
q = 
dp = 
dq = 
c = 

n = p*q
phin = (p-1)*(q-1)
dd = gcd(p-1, q-1)
d=(dp-dq)//dd * invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
print(d)

m = powmod(c, d, n)
print(bytes.fromhex(hex(m)[2:]))

