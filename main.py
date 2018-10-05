from decimal import *

b = 0
a = b+1
d = 0
getcontext().prec = 1000

while True:
    c = b+a
    try:
        golden = Decimal(b+a)/Decimal(a)
    except:
        pass
    b = a
    a = c
    d += 1
    if d == 10000:
        break
print(golden)
