p = 
A = 
B = 
E = EllipticCurve(GF(p),[A,B])
P = E(, )
Q = E(, )
factors, exponents = zip(*factor(E.order()))
primes = [factors[i] ^ exponents[i] for i in range(len(factors))][:-1]
print(primes)
dlogs = []
for fac in primes:
    t = int(int(P.order()) // int(fac))
    dlog = discrete_log(t*Q,t*P,operation="+")
    dlogs += [dlog]
    print("factor: "+str(fac)+", Discrete Log: "+str(dlog)) #calculates discrete logarithm for each prime order
print(crt(dlogs,primes))
