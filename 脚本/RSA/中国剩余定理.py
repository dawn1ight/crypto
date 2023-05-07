from Crypto.Util.number import *
from gmpy2 import *
from functools import reduce

n1 = 
n2 = 
n3 = 
c1 = 
c2 = 
c3 = 

N = []
c = []
for i in range(3):
    N.append(eval('n' + str(i + 1)))
    c.append(eval('c' + str(i + 1)))

def chinese_remainder(modulus, remainders):
    Sum = 0
    prod = reduce(lambda a, b: a * b, modulus)
    for m_i, r_i in zip(modulus, remainders):
        p = prod // m_i
        Sum += r_i * (inverse(p, m_i) * p)
    return Sum % prod

pow_m_e = chinese_remainder(N, c)

#e未知
for e in range(65537):
    try:
        m = iroot(pow_m_e, e)[0]
        f = str(long_to_bytes(m))
        if 'ctf' in f or 'flag' in f:
            print(f)
    except ValueError:
        continue
#e已知
e = 
m = iroot(pow_m_e, e)[0]
print(long_to_bytes(m))
