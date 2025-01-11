import time
import numpy as np
import psutil
from pyspark.sql import SparkSession, Row


spark = SparkSession.builder.master("local[1]").appName(
    "exponenciacionMatrices").getOrCreate()


def generador_matrices(N):
    A = np.zeros((N, N))
    for i in np.arange(0, N):
        for j in np.arange(i, N):
            A[i][j] = np.random.randn(1) * (-1) ** (i + j)
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


def realizar_prueba(row):
    dimension = row['dimension']
    exponente = row['exponente']

    tiempos = []
    cpu_usos = []
    ram_usos = []

    for _ in range(100):
        matriz = generador_matrices(dimension)
        inicio_tiempo_binario = time.time()
        _, cpu_promedio, ram_promedio = exponenciacion_binaria(
            matriz, exponente)
        tiempo_binario = time.time() - inicio_tiempo_binario

        tiempos.append(tiempo_binario)
        cpu_usos.append(cpu_promedio)
        ram_usos.append(ram_promedio)

    return Row(
        dimension=dimension,
        exponente=exponente,
        tiempo_promedio=np.mean(tiempos),
        cpu_promedio=np.mean(cpu_usos),
        ram_promedio=np.mean(ram_usos)
    )


configuraciones = [
    Row(dimension=dimension, exponente=exponente)
    for dimension in range(1, 11)
    for exponente in [1, 301, 501, 701, 901, 1000]
]


config_df = spark.createDataFrame(configuraciones)


resultados = config_df.rdd.map(realizar_prueba).collect()


for resultado in resultados:
    print(f"Matriz {resultado.dimension}x{
          resultado.dimension}, Potencia {resultado.exponente}")
    print(f"Tiempo promedio: {resultado.tiempo_promedio:.6f}s")
    print(f"CPU promedio: {resultado.cpu_promedio:.2f}%")
    print(f"RAM promedio: {resultado.ram_promedio:.2f}%")
    print("-" * 50)


spark.stop()
