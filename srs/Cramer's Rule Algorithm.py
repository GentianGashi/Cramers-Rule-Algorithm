import numpy as np
a = np.array([[(1,0,3),(-1,-1,0),(2,4,1)]])
print (a)

print()
b = np.array([(27,-2,10)])
print (b)

c = np.linalg.solve(a,b)

print()
print ("   X,  Y,  Z")
print (c)
