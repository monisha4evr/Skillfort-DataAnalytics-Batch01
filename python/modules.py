# type:
# 1. build-in (math,datetime)
# 2. user-defined 
# 3. external (numpy, pandas)

# math:

import math
print(math.ceil(12.4))
print(math.ceil(12.6))
print(math.floor(12.4))
print(math.floor(12.6))
print(math.trunc(12.4))

import datetime 
cur_date=datetime.datetime.now()
print(cur_date.year)


from calculation import add,sub,mul,divi
add(1,2,3)
print(sub(1,2))
print(mul(5,7))
print(divi(2,0))
print(divi(2,1))

import calculation 
calculation.add(1,2,3)
print(calculation.sub(1,2))
print(calculation.mul(5,7))
print(calculation.divi(2,0))
print(calculation.divi(2,1))


