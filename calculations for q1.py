import math 
from decimal import Decimal                                                    

k = 10**5
kavg = 10**4
numer = Decimal((kavg**k))*Decimal(math.e**(-kavg))
print(numer)
denom = Decimal(math.factorial(k))
print(denom)
print(numer/denom)
