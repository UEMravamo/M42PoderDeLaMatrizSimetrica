# Autor: Adrian Canadas
# Complejidad: O(n^3 ⋅ k)

def multiplicar_matrices(m1, m2):
    """
    Multiplica dos matrices cuadradas de la misma dimensión.

    Args:
        m1 (list of list of int/float): Primera matriz de dimensión n x n.
        m2 (list of list of int/float): Segunda matriz de dimensión n x n.

    Returns:
        list of list of int/float: Matriz resultado de la multiplicación m1 * m2.
    """
    n = len(m1)  # Dimensión de la matriz

    # Crear una matriz de dimensión n x n inicializada en ceros
    resultado = [[0] * n for _ in range(n)]

    # Recorre cada fila de la primera matriz
    for i in range(n):
        # Recorre cada columna de la segunda matriz
        for j in range(n):
            # Recorre cada elemento de la fila y columna correspondientes
            for k in range(n):
                # Suma el producto de los elementos correspondientes
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado


def elevar_matriz_a_potencia(a, k):
    """
    Eleva una matriz cuadrada a una potencia k usando multiplicaciones repetidas.

    Args:
        a (list of list of int/float): Matriz cuadrada de dimensión n x n.
        k (int): Potencia a la que se desea elevar la matriz.

    Returns:
        list of list of int/float: Matriz resultado a^k.
    """
    n = len(a)  # Dimensión de la matriz

    # Crear matriz identidad (I ⋅ A = A)
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    resultado = identidad  # Inicializamos el resultado como la matriz identidad

    # Realiza k multiplicaciones de matrices
    for _ in range(k):
        resultado = multiplicar_matrices(resultado, a)

    return resultado


# Matriz A
A = [
    [2, 1, -1],
    [1, 0, 1],
    [-1, 1, 2]
]

# Potencia a la que se elevará la matriz
k = 4

# Calcular A elevado a k
Ak = elevar_matriz_a_potencia(A, k)

# Imprimir el resultado
print("Matriz A^4:")
for fila in Ak:
    print(fila)
