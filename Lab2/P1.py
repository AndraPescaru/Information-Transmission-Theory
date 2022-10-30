import numpy as np

T = np.asanyarray([[0.25, 0.5, 0.25],
                   [0.5, 0.25, 0.25],
                   [0.25, 0.25, 0.5]])

print(T)

p0 = list(map(float, input() .split()))
print (p0)

p1 = p0 @ T
print(p1)

p7 = p0 @ np.linalg.matrix_power(T, 7)
print (p7)

