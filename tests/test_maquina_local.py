import time
import psutil
import numpy as np
import csv

ruta_csv = "./rendimiento_matrices2.csv"

with open(ruta_csv, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["Dimension", "Potencia", "Tiempo Promedio (s)",
                    "CPU Promedio (%)", "RAM Promedio (%)"])


def generador_matrices(N):
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(i, N):
            A[i][j] = np.random.randn() * (-1) ** (i + j)
            A[j][i] = A[i][j]
    return np.round(A + np.diag(np.ones(N)), 2)


def ram_usada():
    proceso = psutil.Process()  # Obtenemos el proceso actual
    # Cogemos la ram utilizada por el programa
    memoria_usada = proceso.memory_info().rss
    memoria_total = psutil.virtual_memory().total  # Cogemos la ram de mi ordenador
    porcentaje_usado = (memoria_usada / memoria_total) * 100
    return porcentaje_usado


def exponenciacion_binaria(matriz, potencia):
    potencia_binaria = bin(potencia)[2:]
    rv = np.eye(len(matriz))
    pre = matriz

    # Inicializamos listas para capturar el uso de CPU y RAM
    cpu_usos = []
    ram_usos = []

    for bit in reversed(potencia_binaria):
        # Registrar CPU y RAM antes de realizar cálculos
        cpu_usos.append(psutil.cpu_percent(interval=0.001))
        ram_usos.append(ram_usada())

        if bit == "1":
            rv = np.dot(rv, pre)
        pre = np.dot(pre, pre)

    # devolvemos la matriz calculada, el uso de de la cpu y de la ram
    return np.round(rv, 2), np.mean(cpu_usos), np.mean(ram_usos)


def medir_rendimiento(dimension, exponente):
    """
    Realiza la medición del rendimiento para una matriz de tamaño dado y potencia.
    """
    print(f"Matriz de tamaño {dimension}x{dimension} de potencia {exponente}")
    tiempos = []
    cpu_interaciones = []
    ram_interaciones = []

    for _ in range(100):  # Repetimos 100 veces para obtener promedios
        matriz = generador_matrices(dimension)
        inicio_tiempo = time.time()

        # Llamamos a la función de exponenciación binaria
        _, cpu_promedio, ram_promedio = exponenciacion_binaria(
            matriz, exponente)

        tiempo_total = time.time() - inicio_tiempo
        tiempos.append(tiempo_total)
        cpu_interaciones.append(cpu_promedio)
        ram_interaciones.append(ram_promedio)

    # Calculamos las medias
    tiempo_medio = np.mean(tiempos)
    cpu_medio = np.mean(cpu_interaciones)
    ram_medio = np.mean(ram_interaciones)

    # Imprimimos los resultados en la terminal
    print(f"Tiempo promedio: {tiempo_medio:.6f}s | CPU : {
          cpu_medio:.2f}% | RAM : {ram_medio:.2f}%")
    print("*******************************")

    # Guardamos los resultados en el archivo CSV
    with open(ruta_csv, mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(
            [dimension, exponente, tiempo_medio, cpu_medio, ram_medio])


# Probamos las matrices de 1x1 a 10x10 con potencias de 100 a 1000
dimensiones = range(1, 11)
potencias = range(100, 1001, 100)

for dimension in dimensiones:
    print(f"\n--- Probando matriz {dimension}x{dimension} ---")
    for potencia in potencias:
        medir_rendimiento(dimension, potencia)
