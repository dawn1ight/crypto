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
