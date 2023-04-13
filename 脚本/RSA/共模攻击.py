#共模攻击
import gmpy2
from Crypto.Util.number import long_to_bytes

e1 = 
e2 = 
n  = 
c1 = 
c2 = 


_, r, s = gmpy2.gcdext(e1, e2)

m = pow(c1, r, n) * pow(c2, s, n) % n
print (long_to_bytes(m))
