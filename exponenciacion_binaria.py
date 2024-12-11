import numpy as np


def generador_matrices(N):
    A = np.zeros((N, N))

    for i in np.arange(0, N):
        for j in np.arange(i, N):
            A[i][j] = np.random.randn(1)*(-1)**(i+j)
            A[j][i] = A[i][j]

    return np.round(A + np.diag(np.ones(N)), 2)


def exponenciacion_binaria(matriz, potencia):
    potencia = bin(potencia)[2:]
    rv = np.eye(len(matriz))
    pre = matriz
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
