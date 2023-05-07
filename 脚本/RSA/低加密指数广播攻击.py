from sympy.ntheory.modular import crt
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

e = 
N = []
C =  []

assert len(N) == e
assert len(C) == e

resultant, mod = crt(N,C)
value, is_perfect = iroot(resultant,e)
print(long_to_bytes(value))
