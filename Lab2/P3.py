import numpy as np

T = np.asanyarray([[0.01, 0.98, 0.01],
                   [0.98, 0.01, 0.01],
                   [0.01, 0.01, 0.98]])

p0 = list(map(float, input() .split()))

lista = np.asanyarray([])

for i in range(8):
    p = p0 @ np.linalg.matrix_power(T, i+1)
    lista = np.append(lista, p[2])
    
for i in range(len(lista)):
        
    print('%.3f' %lista[i], end = ' ')
    



  
    
