import numpy as np

def genmatrix_sim(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            A[i, j] = np.random.randn(1) * (-1) ** (i + j)
            A[j, i] = A[i, j]
    A += np.diag(np.ones(n))
    return A

def mult_matrix(A, B):
    n = len(A)  
    mult = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mult[i][j] += A[i][k] * B[k][j]
    return mult

def matrix_idnt(n):
    idnt = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        idnt[i][i] = 1
    return idnt


def round_matrix(A, x):
    n = len(A)
    for i in range(n):
        for j in range(n):
            A[i][j] = round(A[i][j], x)
    return A


def matrix_sim(A, K):
    """
    basciamente rehehcho el codigo hecho en test para matrix_sim3 pero sin usar numpy
    """
   
    n = len(A)  
    
    # caso base-> si el exponente es 0 devolvemos la matriz identidad
    if K == 0:
        return matrix_idnt(n)
    # si el exponenet es impar multiplicamos por la matriz original
    if K % 2 == 1:
        return mult_matrix(A, matrix_sim(A, K - 1))
    # en caso contrrio es par  por lo que calculamos la mitad de la potencia y multiplicamos por si misma
    mitad = matrix_sim(A, K // 2)
    return round_matrix(mult_matrix(mitad, mitad), 2) 
def matrix_sim3(A,K):
    """
    Otra manera para mantener la complejidad O(log(n)·m³)
    """
    # caso base-> si el exponente es 0 devolvemos la matriz identidad
    if K == 0:
        return np.eye(len(A))
    
    # si el exponenet es impar multiplicamos por la matriz original
    if K % 2 == 1:
        return np.dot(A, matrix_sim3(A, K-1))
    
    ## en caso contrrio es par  por lo que calculamos la mitad de la potencia y multiplicamos por si misma
    temp = matrix_sim3(A, K//2)
    return np.round(np.dot(temp, temp),2)##para cumplir con los requisitos 
if __name__ == "__main__":
    
    print("Generar matriz:")
    A = genmatrix_sim(3)
    print(np.round(A, 2))#requisito ya que debemos redondear a 2 decimales 
    K = 2
    print("Resultado: ")
    resultado = matrix_sim(A, K)
    print(resultado)
    print("Resultado: ")
    resultado2 = matrix_sim3(A, K)
    print(resultado2)
    if np.array_equal(resultado, resultado2):#comprobamos que el resultado es el mismo o no 
        print("Los resultados son iguales.")
    else:
        print("Los resultados son diferentes.")