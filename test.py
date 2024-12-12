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
def matrix_sim(A,K):##cambio la n no hacia falta 
    for k in range(K):
        A = np.dot(A, A)
    
    return np.round(A, 2)#requisito ya que debemos redondear a 2 decimales 
def matrix_sim2(A, K):#otra manera de hacerlo 
    A = np.linalg.matrix_power(A, 2 ** K)
    return np.round(A, 2)#Seguimos sin estar en la complejidad deseada 
if __name__ == "__main__":
    
    print("Generar matriz:")
    A = genmatrix_sim(3)
    print(np.round(A, 2))#requisito ya que debemos redondear a 2 decimales 
    K = 2
    print("Resultado: ")
    resultado = matrix_sim(A, K)
    print(resultado)
    print("Resultado 2:")
    resultado2 =matrix_sim2(A,K)
    print(resultado2)
    if np.array_equal(resultado, resultado2):#comprobamos que el resultado es el mismo o no 
        print("Los resultados son iguales.")
    else:
        print("Los resultados son diferentes.")
    

    




 
