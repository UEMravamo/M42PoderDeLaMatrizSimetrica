

import time
import numpy as np
import matplotlib.pyplot as plt
import csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import unittest


# Funciones principales
def generador_matrices(n):
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            matriz[i][j] = np.random.randn() * (-1) ** (i + j)
            matriz[j][i] = matriz[i][j]
    return np.round(matriz + np.diag(np.ones(n)), 2)


def exponenciacion_binaria(matriz, exponente):
    exponente_binario = bin(exponente)[2:]
    resultado = np.eye(len(matriz))
    matriz_potencia = matriz.copy()

    for bit in reversed(exponente_binario):
        if bit == '1':
            resultado = np.dot(resultado, matriz_potencia)
        matriz_potencia = np.dot(matriz_potencia, matriz_potencia)

    return np.round(resultado, 2)


def medir_tiempo_local(dimension, exponente):
    matriz = generador_matrices(dimension)
    inicio = time.time()
    exponenciacion_binaria(matriz, exponente)
    fin = time.time()
    return fin - inicio


def medir_tiempo_distribuido(dimension, exponente, spark):
    if dimension <= 1000:
        return medir_tiempo_local(dimension, exponente)

    matriz = generador_matrices(dimension)
    rdd = spark.sparkContext.parallelize(matriz.tolist(), numSlices=8)

    def procesar_particiones(particion):
        particion_lista = list(particion)
        if len(particion_lista) == 0:
            return []
        try:
            matriz_parcial = np.array(particion_lista)
            resultado = exponenciacion_binaria(matriz_parcial, exponente)
            return [resultado.tolist()]
        except Exception as e:
            print(f"Error procesando partición: {e}")
            return []

    inicio = time.time()
    resultado_rdd = rdd.mapPartitions(procesar_particiones)
    resultado_rdd.collect()
    fin = time.time()
    return fin - inicio


def comparar_rendimiento(configuraciones, spark):
    tiempos_local = []
    tiempos_distribuido = []

    with open("resultados_rendimiento.csv", "w", newline="") as csvfile:
        fieldnames = ["Dimension", "Exponente", "Tiempo Local", "Tiempo Distribuido"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for dimension, exponente in configuraciones:
            tiempo_local = medir_tiempo_local(dimension, exponente)
            tiempo_distribuido = medir_tiempo_distribuido(dimension, exponente, spark)

            tiempos_local.append(tiempo_local)
            tiempos_distribuido.append(tiempo_distribuido)

            print(f"Dimensión: {dimension}x{dimension}, Exponente: {exponente}")
            print(f"Tiempo Local: {tiempo_local:.6f} segundos")
            print(f"Tiempo Distribuido: {tiempo_distribuido:.6f} segundos")
            print("-" * 50)

            writer.writerow({
                "Dimension": dimension,
                "Exponente": exponente,
                "Tiempo Local": tiempo_local,
                "Tiempo Distribuido": tiempo_distribuido
            })

    return tiempos_local, tiempos_distribuido


def graficar_resultados(configuraciones, tiempos_local, tiempos_distribuido):
    dimensiones = [dim for dim, _ in configuraciones]

    plt.figure(figsize=(10, 6))
    plt.plot(dimensiones, tiempos_local, label="Tiempo Local", marker="o")
    plt.plot(dimensiones, tiempos_distribuido, label="Tiempo Distribuido", marker="s")
    plt.xlabel("Tamaño de la Matriz (N x N)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de Rendimiento: Local vs Distribuido")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparacion_rendimiento.png")
    plt.show()


# Bloque principal
if __name__ == "__main__":
    configuraciones = [
        (10, 2), (20, 3), (30, 4), (40, 5), (50, 6),
        (100, 3), (200, 4), (300, 5), (400, 6), (500, 7),
        (1000, 3), (2000, 4), (3000, 5), (4000, 6), (5000, 7)
    ]

    spark = SparkSession.builder \
        .appName("ComparacionRendimientoMatrices") \
        .master("local[8]") \
        .getOrCreate()

    tiempos_local, tiempos_distribuido = comparar_rendimiento(configuraciones, spark)
    graficar_resultados(configuraciones, tiempos_local, tiempos_distribuido)
    spark.stop()


# Pruebas
class TestGeneradorMatrices(unittest.TestCase):

    def test_dimensiones(self):
        matriz = generador_matrices(5)
        self.assertEqual(matriz.shape, (5, 5))

    def test_simetria(self):
        matriz = generador_matrices(5)
        self.assertTrue((matriz == matriz.T).all())


class TestExponenciacionBinaria(unittest.TestCase):

    def test_identidad(self):
        matriz = np.eye(3)
        resultado = exponenciacion_binaria(matriz, 3)
        self.assertTrue((resultado == matriz).all())

    def test_potencia(self):
        matriz = np.array([[2, 0], [0, 2]])
        resultado = exponenciacion_binaria(matriz, 3)
        esperado = np.array([[8, 0], [0, 8]])
        self.assertTrue((resultado == esperado).all())


if __name__ == "__main__":
    import sys
    if 'unittest' in sys.argv[0]:
        unittest.main()



    """ 
    Dimensión: 10x10, Exponente: 2
    Tiempo Local: 0.000079 segundos
    Tiempo Distribuido: 0.000037 segundos
    --------------------------------------------------
    Dimensión: 20x20, Exponente: 3
    Tiempo Local: 0.000872 segundos
    Tiempo Distribuido: 0.000038 segundos
    --------------------------------------------------
    Dimensión: 30x30, Exponente: 4
    Tiempo Local: 0.000100 segundos
    Tiempo Distribuido: 0.000063 segundos
    --------------------------------------------------
    Dimensión: 40x40, Exponente: 5
    Tiempo Local: 0.000146 segundos
    Tiempo Distribuido: 0.000094 segundos
    --------------------------------------------------
    Dimensión: 50x50, Exponente: 6
    Tiempo Local: 0.000191 segundos
    Tiempo Distribuido: 0.000118 segundos
    --------------------------------------------------
    Dimensión: 100x100, Exponente: 3
    Tiempo Local: 0.000567 segundos
    Tiempo Distribuido: 0.000492 segundos
    --------------------------------------------------
    Dimensión: 200x200, Exponente: 4
    Tiempo Local: 0.002757 segundos
    Tiempo Distribuido: 0.004847 segundos
    --------------------------------------------------
    Dimensión: 300x300, Exponente: 5
    Tiempo Local: 0.010439 segundos
    Tiempo Distribuido: 0.015720 segundos
    --------------------------------------------------
    Dimensión: 400x400, Exponente: 6
    Tiempo Local: 0.027946 segundos
    Tiempo Distribuido: 0.023388 segundos
    --------------------------------------------------
    Dimensión: 500x500, Exponente: 7
    Tiempo Local: 0.053081 segundos
    Tiempo Distribuido: 0.054131 segundos
    --------------------------------------------------
    Dimensión: 1000x1000, Exponente: 3
    Tiempo Local: 0.287057 segundos
    Tiempo Distribuido: 0.281263 segundos
    --------------------------------------------------
    Dimensión: 2000x2000, Exponente: 4
    Tiempo Local: 3.176151 segundos
    Tiempo Distribuido: 2.952913 segundos
    --------------------------------------------------
    Dimensión: 3000x3000, Exponente: 5
    Tiempo Local: 9.860844 segundos
    Tiempo Distribuido: 3.739678 segundos
    --------------------------------------------------
    Dimensión: 4000x4000, Exponente: 6
    Tiempo Local: 21.843653 segundos
    Tiempo Distribuido: 3.341801 segundos
    --------------------------------------------------
    Dimensión: 5000x5000, Exponente: 7
    Tiempo Local: 52.425004 segundos
    Tiempo Distribuido: 6.221384 segundos
    -------------------------------------------------- 
    """