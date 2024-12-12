import numpy as np


def generador_matrices(N):
    A = np.zeros((N, N))

    for i in np.arange(0, N):
        for j in np.arange(i, N):
            A[i][j] = np.random.randn(1)*(-1)**(i+j)
            A[j][i] = A[i][j]

    return np.round(A + np.diag(np.ones(N)), 2)


def exponenciacion_binaria(matriz, potencia):
    """ 
    Primer paso, convertimos el exponente a binario, pongamos 9 como ejemplo.
    9 -> 1001
    Tras esto, empezamos recorriendo desde el bit menos significativo y cada uno
    de ellos que tenga un uno sera el valor que usaremos para multiplicar y elevar.

    1 -> 1 * X^(2^0) = 1 * X^1 
    0 -> 0 * X^(2^1) = 0 * X^2
    0 -> 0 * X^(2^2) = 0 * X^4
    1 -> 1 * X^(2^3) = 1 * X^8

    x^9 = X^1 * X^8

    La variable pre almacena la potencia del indice de la exponencia binaria, 
    haciendo que en cada iteración, se actualiza al cuadrado y si el bit
    es 1 lo multiplicamos con rv. Con esto se consigue que el algoritmo
    sea eficiente, con magnitud O(log(n)).
    """
    potencia = bin(potencia)[2:]  # bin(X) -> 0bXXXXX. Retiramos prefijo
    rv = np.eye(len(matriz))  # Matriz identidad de una matrix NxN
    pre = matriz
    # Orden inverso para empezar por el bit menos significativo.
    for bit in reversed(potencia):
        if bit == "1":
            rv = np.dot(rv, pre)
        pre = np.dot(pre, pre)

    return np.round(rv, 2)


potencia = 13
size_matriz = 5
A = generador_matrices(size_matriz)
result = exponenciacion_binaria(A, potencia)
expected_result = np.round(np.linalg.matrix_power(A, potencia), 2)
print("Deberia dar\n", expected_result)
print("Resultado Calculado\n", result)
test = np.allclose(result, expected_result, atol=1e-3)
print(test)
