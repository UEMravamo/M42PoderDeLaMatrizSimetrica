def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices cuadradas A y B.

    Args:
        A (list[list[int]]): Primera matriz.
        B (list[list[int]]): Segunda matriz.

    Returns:
        list[list[int]]: Matriz resultante de la multiplicación A x B.
    """
    n = len(A)
    resultado = []
    for i in range(n):
        fila = []
        for j in range(n):
            suma = sum(A[i][k] * B[k][j] for k in range(n))
            fila.append(suma)
        resultado.append(fila)
    return resultado


def matriz_identidad(n):
    """
    Crea una matriz identidad de tamaño n x n.

    Args:
        n (int): Dimensión de la matriz identidad.

    Returns:
        list[list[int]]: Matriz identidad.
    """
    identidad = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        identidad.append(fila)
    return identidad


def potencia_matrizrecursiva(matriz, exponente):
    """
    Calcula la potencia de una matriz cuadrada usando recursividad.

    Args:
        matriz (list[list[int]]): Matriz base.
        exponente (int): Potencia a la que se eleva la matriz.

    Returns:
        list[list[int]]: Matriz elevada a la potencia exponente.
    """
    if exponente == 0:
        return matriz_identidad(len(matriz))
    if exponente == 1:
        return matriz


    mitad = potencia_matrizrecursiva(matriz, exponente // 2)
    mitad_cuadrada = multiplicar_matrices(mitad, mitad)

    if exponente % 2 == 0:
        return mitad_cuadrada
    else:
        return multiplicar_matrices(mitad_cuadrada, matriz)


# Ejemplo
matriz = [
    [2, 1, -1],
    [1, 0, 1],
    [-1, 1, 2]
]
exponente = 4
matriz_potencia = potencia_matrizrecursiva(matriz, exponente)


for fila in matriz_potencia:
    print(fila)