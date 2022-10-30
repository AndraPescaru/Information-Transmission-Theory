import numpy as np

N, K = map(int, input() .split())

p0 = np.full((K), 1/K)

T = np.asanyarray([])

for i in range(K):
    
    p = list(map(float, input() .split()))
    T = np.concatenate((T , p), axis = 0)
matrix = np.array(T).reshape(K,K)    
     
z1=np.asanyarray([])

for i in range(N):
    p = p0 @ np.linalg.matrix_power(matrix, i)
    z1 = np.concatenate((z1, p), axis = 0)
    
z2 = np.array(z1).reshape(N, K)
z3 = z2.transpose()

control = 0    
diff = 0  
  
for i in range(K):
    
    for j in range(N):
       if j==0 : 
          diff = z3[i][0]
                 
       else:
          diff = z3[i][j] - z3[i][j-1]
                    
       if abs(diff) < pow(10, -3):
         control = True
         
       else: 
         control = False
         
print (control)
        
        
    
    
    
