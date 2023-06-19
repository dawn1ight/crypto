# x=pow(m,p,n)
# y=pow(m,q,n)

import libnum
x = 
y = 
n =
p = libnum.gcd(pow(x,n)-y,y)
q = n//p
d = libnum.invmod(p,(p-1)*(q-1))
print(libnum.n2s(pow(x,d,n)))

# P = pow(m, p, n)
# Q = pow(m, q, n)
# R = pow(m, r, n)

n=
P=
Q=
R=
PR.<m> = PolynomialRing(Zmod(n))
f = -m^3+(P+Q+R)*m^2-(P*Q+P*R+R*Q)*m+P*Q*R
m = f.monic().small_roots(X=2^256)
print(m)
