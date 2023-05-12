#https://lazzzaro.github.io/2020/05/06/crypto-RSA/
#sage

from gmpy2 import *
e0=
n0=
c0=
e1=
n1=
c1=
e2=
n2=
c2=

M=iroot(int(n2),int(2))[0]
a=[0]*4
a[0]=[M,e0,e1,e2]
a[1]=[0,-n0,0,0]
a[2]=[0,0,-n1,0]
a[3]=[0,0,0,-n2]

Mat = matrix(ZZ,a)
Mat_LLL=Mat.LLL()
d = abs(Mat_LLL[0][0])/M
print(bytes.fromhex(hex(pow(c1,int(d),int(n1)))[2:]))
