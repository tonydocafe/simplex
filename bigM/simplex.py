import numpy as np

def simplex(A, b, c):

    m, n = A.shape
    B = np.eye(m)
    xB = np.linalg.solve(B, b)
    
    while True:
        custos_reduzidos = c - np.dot(np.dot(c[:m], np.linalg.inv(B)), A)
        
        if np.all(custos_reduzidos >= 0):
            print("Solução ótima encontrada!")
            break
        
       
        j = np.argmin(custos_reduzidos)
        col = A[:, j]
        
    
        
        if np.all(ratios == np.inf):
            print("Problema ilimitado.")
            break
        
    
        i = np.argmin(ratios)
        
   
        B[:, i] = A[:, j]
        xB = np.linalg.solve(B, b)
    
    return xB

