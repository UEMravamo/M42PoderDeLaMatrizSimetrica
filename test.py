import numpy as np

def genmatrix_sim(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            A[i, j] = np.random.randn(1) * (-1) ** (i + j)
            A[j, i] = A[i, j]
    A += np.diag(np.ones(n))
    return A

#Realizar logica del  la matriz
def matrix_sim(n,A,K):
    
    return 0

if __name__ == "__main__":
    
    print("Generar matriz:")
    A = genmatrix_sim(3)
    print(A)

   

    




 
