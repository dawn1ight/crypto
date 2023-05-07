import gmpy2
from Crypto.Util.number import long_to_bytes

n =
e =       
c =    

for k in range(200000000):    #参数可调
    if gmpy2.iroot(c+n*k,e)[1]==1:    #开n次根
        res=gmpy2.iroot(c+n*k,e)[0]    
        print(long_to_bytes(res))    
        break
