from gmpy2 import *
from Crypto.Util.number import long_to_bytes

e = 
n = 
dp = 
c = 

for x in range(1, e):
	if(e*dp%x==1):
		p=(e*dp-1)//x+1
		if(n%p!=0):
			continue
		q=n//p
		phin=(p-1)*(q-1)
		d=invert(e, phin)
		m=powmod(c, d, n)
		if(len(hex(m)[2:])%2==1):
			continue
		print(long_to_bytes(m))
