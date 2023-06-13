def solve_pell(N, numTry = 1500):
    cf = continued_fraction(sqrt(N))    
    for i in range(numTry):
        denom = cf.denominator(i)
        numer = cf.numerator(i)        
        if numer^2 - N * denom^2 == 1:            
            return numer, denom    
    return None, None
