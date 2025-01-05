import time
import numpy as np
import psutil
from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local[1]").appName("exponenciacionMatrices").getOrCreate()

def generador_matrices(N):
    A = np.zeros((N, N))

    for i in np.arange(0, N):
        for j in np.arange(i, N):
            A[i][j] = np.random.randn(1) * (-1)**(i + j)
            A[j][i] = A[i][j]

    return np.round(A + np.diag(np.ones(N)), 2)

def exponenciacion_binaria(matriz, potencia):
    potencia = bin(potencia)[2:]
    rv = np.eye(len(matriz))
    pre = matriz
    tiempos_cpu = []
    tiempos_ram = []

    for bit in reversed(potencia):

        cpu_actual = psutil.cpu_percent(interval=0.001)
        ram_actual = psutil.virtual_memory().percent
        tiempos_cpu.append(cpu_actual)
        tiempos_ram.append(ram_actual)

        if bit == "1":
            rv = np.dot(rv, pre)
        pre = np.dot(pre, pre)

    return np.round(rv, 2), np.mean(tiempos_cpu), np.mean(tiempos_ram)


def medir_rendimiento(dimension, exponente):
    print(f"Matriz de tamaño {dimension}x{dimension} de potencia {exponente}")

    tiempos = []
    cpu_usos = []
    ram_usos = []


    for _ in range(100):
        matriz = generador_matrices(dimension)
        inicio_tiempo_binario = time.time()
        _, cpu_promedio, ram_promedio = exponenciacion_binaria(matriz, exponente)
        tiempo_binario = time.time() - inicio_tiempo_binario

        tiempos.append(tiempo_binario)
        cpu_usos.append(cpu_promedio)
        ram_usos.append(ram_promedio)


    tiempo_medio = np.mean(tiempos)
    cpu_medio = np.mean(cpu_usos)
    ram_medio = np.mean(ram_usos)

    print(f"Tiempo promedio de ejecución: {tiempo_medio:.6f} segundos")
    print(f"Media de uso de CPU durante las pruebas: {cpu_medio:.2f}%")
    print(f"Media de uso de RAM durante las pruebas: {ram_medio:.2f}%")
    print("-" * 50)


configuraciones = [
    (1, 1), (1, 301), (1, 501), (1, 701), (1, 901), (1, 1000),
    (2, 1), (2, 301), (2, 501), (2, 701), (2, 901), (2, 1000),
    (3, 1), (3, 301), (3, 501), (3, 701), (3, 901), (3, 1000),
    (4, 1), (4, 301), (4, 501), (4, 701), (4, 901), (4, 1000),
    (5, 1), (5, 301), (5, 501), (5, 701), (5, 901), (5, 1000),
    (6, 1), (6, 301), (6, 501), (6, 701), (6, 901), (6, 1000),
    (7, 1), (7, 301), (7, 501), (7, 701), (7, 901), (7, 1000),
    (8, 1), (8, 301), (8, 501), (8, 701), (8, 901), (8, 1000),
    (9, 1), (9, 301), (9, 501), (9, 701), (9, 901), (9, 1000),
    (10, 1), (10, 301), (10, 501), (10, 701), (10, 901), (10, 1000)
]


for dimension, exponente in configuraciones:
    medir_rendimiento(dimension, exponente)


spark.stop()

