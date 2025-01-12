import numpy as np
import time


def generador_matrices(N):
    A = np.zeros((N, N))

    for i in np.arange(0, N):
        for j in np.arange(i, N):
            A[i][j] = np.random.randn() * (-1) ** (i + j)
            A[j][i] = A[i][j]

    return np.round(A + np.diag(np.ones(N)), 2)


def exponenciacion_binaria(matriz, potencia):
    potencia = bin(potencia)[2:]  # bin(X) -> 0bXXXXX. Retiramos prefijo
    # Matriz identidad de una matrix NxN # This line had an extra space, removed it to align with the function definition
    rv = np.eye(len(matriz))
    pre = matriz
    # Orden inverso para empezar por el bit menos significativo.
    for bit in reversed(potencia):
        if bit == "1":
            rv = np.dot(rv, pre)
        pre = np.dot(pre, pre)

    return np.round(rv, 2)
# Evaluación en casos prácticos


def evaluar_casos_practicos():
    casos = [
        {"N": 2, "k": 5},
        {"N": 5, "k": 10},
        {"N": 10, "k": 50}
    ]

    resultados = []

    for caso in casos:
        N, k = caso["N"], caso["k"]
        print(f"Evaluando matriz {N}x{N} elevada a la potencia {k}")

        # Generar matriz simétrica
        A = generador_matrices(N)
        print(f"Matriz generada:\n{A}")
        # Ejecutar 100 veces y calcular el promedio del tiempo
        tiempos = []
        resultado_final = None
        for _ in range(100):
            inicio = time.time()
            Ak = exponenciacion_binaria(A, k)
            fin = time.time()
            tiempos.append(fin - inicio)
            resultado_final = Ak  # Guardamos el último resultado

        promedio_tiempo = sum(tiempos) / len(tiempos)

        # Guardar resultados
        print(f"Resultado:\n{resultado_final}")
        print(f"Promedio del tiempo de ejecución: {
              promedio_tiempo:.4f} segundos\n")

        resultados.append(
            {"N": N, "k": k, "tiempo_promedio": promedio_tiempo, "resultado": resultado_final})

    return resultados


# Ejecutar la evaluación
resultados = evaluar_casos_practicos()
