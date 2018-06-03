import math

def primecheck(limit):
    primes=[]
    divisor=0
    if limit < 2:
        return (0)
    else:
        for i in range(2,limit):
            divisor = 0
            for j in range(2,int(math.ceil(i/2))+1):
                if divisor > 0:
                    continue
                elif i%j == 0:
                    divisor+=1
                    continue
                else:
                    continue
            if divisor == 0:
                primes.append(i)
    return (primes)


c=primecheck(2)
print(c)
