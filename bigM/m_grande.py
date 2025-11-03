import numpy as np
from scipy.optimize import linprog

def resolver(tipo, A, b, sinais, c, metodo="m-grande"):
    m, n = A.shape
    artificiais = []
    
    
    num_folgas = sum(1 for sinal in sinais if sinal == "<")
    num_excessos = sum(1 for sinal in sinais if sinal == ">")
    num_artificiais = sum(1 for sinal in sinais if sinal == ">" or sinal == "=")
    
    total_variaveis = n + num_folgas + num_excessos + num_artificiais
    
   
    A_mod = np.zeros((m, total_variaveis))
    A_mod[:, :n] = A
    
    
    idx_folga = n
    idx_excesso = n + num_folgas
    idx_artificial = n + num_folgas + num_excessos
    
#preencher variáveis auxiliares
    for i, sinal in enumerate(sinais):
        if sinal == "<":
            A_mod[i, idx_folga] = 1
            idx_folga += 1
        elif sinal == ">":
            A_mod[i, idx_excesso] = -1
            A_mod[i, idx_artificial] = 1
            artificiais.append(idx_artificial)
            idx_excesso += 1
            idx_artificial += 1
        elif sinal == "=":
            A_mod[i, idx_artificial] = 1
            artificiais.append(idx_artificial)
            idx_artificial += 1

   
    c_mod = np.zeros(total_variaveis)
    c_mod[:n] = c
    
    
    if metodo == "m-grande":
        M = 1000  
        
        for idx in artificiais:
            if tipo == "max":
                c_mod[idx] = -M  
            else:
                c_mod[idx] = M   

        if tipo == "max":
            c_mod = -c_mod  

        res = linprog(c_mod, A_eq=A_mod, b_eq=b, method="highs")
        
        if res.success:
            for idx in artificiais:
                if abs(res.x[idx]) > 1e-6:  
                    print(f"Aviso: Variável artificial {idx} = {res.x[idx]} (deveria ser 0)")
        
        return res
