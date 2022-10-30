import numpy as np

p0 = np.asanyarray([1, 0, 0])

p = float(input())

T = np.asanyarray([[(p), (1.0-2.0*p), (p)],
                   [(1.0-2.0*p), (p), (p)],
                   [(p), (p), (1.0-2.0*p)]])

print (T)

p5 = p0 @ np.linalg.matrix_power(T, 5)
print (p5)
print (p5[1])



