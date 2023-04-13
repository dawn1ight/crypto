import gmpy2
from Crypto.Util.number import long_to_bytes
n1 = 
n2 = 
q = gmpy2.gcd(n1,n2)
p = n1//q
e = 
phi = (p-1)*(q-1)
d = gmpy2.invert(e, phi)
m = pow(c, d, n) 
print(long_to_bytes(m))
