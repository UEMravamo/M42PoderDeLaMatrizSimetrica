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
def matrix_sim(A, K):
    A = np.linalg.matrix_power(A,K)#COrreccion ya que no lo estaba haciendo lo que se pedia, ahora si.
    return np.round(A, 2)#pese a ello  sin estar en la complejidad deseada O(log(K) * m^3) y estamos en K*m^3.

def matrix_sim2(A, K):#nueva manera  con la complejidad: O(log(K) * m^3).
    """
    En los pasados codigos no conseguia obtener la manera optima para lograr la complejidad que queria que era O(log(K) * m^3)
    y tenia (k*m^3), y tras investigar la mejor manera para hacerlo es  usando  exponenciacion binaria ya que esta tecniac 
    se basa en la propiedad de asociatividad de la multiplicación y no requiere propiedades adicionales puede ser la simetiar o diagonalizacion.
    """
    n = A.shape[0]
    final = np.eye(n)
    while K > 0:## En esta parte aplicamos la expoenciacion binaria
        if K % 2 == 1:
            final = np.dot(final, A)
        A = np.dot(A, A)
        K = K // 2
    return np.round(final, 2)##para cumplir con los requisitos 
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
    

    




 
