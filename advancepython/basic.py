import numpy as np
a=[1,2,3,4]
print(type(a))
a=np.array(a)
print(type(a))
print((a.dtype))

a=[1,2,3,4]
a=np.array(a,np.float32)
print(a.dtype)
a=a.astype(np.int8)
print(a.dtype)
print(a)

a=['true','false']
print(type(a))
a=np.array(a,np.bool_)
print(a.dtype)

import numpy as np
a = np.linspace(1, 10, 2)
print(a)

import numpy as np
a = np.linspace(1, 5, 5, dtype=int)
print(a)
a = np.linspace(1, 5, 5, dtype=float)
print(a)

import numpy as np
print(np.eye(5,3, k=4))


1.np.eye() Vs np.identity()
2. shape vs reshape


Rand:
rand → Random decimal between 0 and 1
randn → Random decimal from Normal distribution (negative, positive, or zero)
randint → Random integer


import numpy as np
a=[300,120,340,500]
a=np.array(a,dtype=np.int8)
print(a)

import numpy as np
print(np.__version__)

a = [210, 20, -130, 40, 50]
print(np.array(a, dtype=np.int8))

a = [180, 90, 10]
print(np.array(a, dtype=np.int8))

