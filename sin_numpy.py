def multiplicar_matrices(M1, M2):
    n = len(M1)
    resultado = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += M1[i][k] * M2[k][j]
    return resultado

def elevar_matriz_a_potencia(A, k):
    n = len(A)
    resultado = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Matriz identidad
    for _ in range(k):
        resultado = multiplicar_matrices(resultado, A)
    return resultado

# Matriz A
A = [
    [2, 1, -1],
    [1, 0, 1],
    [-1, 1, 2]
]
k = 4
Ak = elevar_matriz_a_potencia(A, k)

# Imprimir el resultado
print("Matriz A^4:")
for fila in Ak:
    print(fila)
