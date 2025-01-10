import time
import numpy as np
from pyspark.sql import SparkSession

# ============== FUNCIONES BASE ==============

def generar_matriz_simetrica(n):
    """Genera una matriz simétrica aleatoria de tamaño n x n."""
    M = np.random.randn(n, n)
    M = (M + M.T) / 2
    np.fill_diagonal(M, M.diagonal() + 1)  # Asegura diagonales positivas
    return np.round(M, 2)

def exponenciacion_binaria_local(A, k):
    """Eleva una matriz a la potencia k usando exponenciación binaria."""
    n = len(A)
    res = np.eye(n)
    base = A
    while k:
        if k % 2:
            res = np.dot(res, base)
        base = np.dot(base, base)
        k //= 2
    return np.round(res, 2)

def exponenciacion_binaria_distribuida(spark, A, k):
    """Eleva una matriz a la potencia k utilizando PySpark para operaciones distribuidas."""
    n = len(A)
    R = np.eye(n)
    base = A
    while k:
        if k % 2:
            R = np.dot(R, base)
        base = np.dot(base, base)
        k //= 2
    return np.round(R, 2)

def medir_rendimiento_local(A, k):
    """Mide el tiempo de ejecución de la exponenciación binaria en modo local."""
    inicio = time.time()
    resultado = exponenciacion_binaria_local(A, k)
    tiempo = time.time() - inicio
    return resultado, tiempo

def medir_rendimiento_distribuido(spark, A, k):
    """Mide el tiempo de ejecución de la exponenciación binaria en modo distribuido con PySpark."""
    inicio = time.time()
    resultado = exponenciacion_binaria_distribuida(spark, A, k)
    tiempo = time.time() - inicio
    return resultado, tiempo

# ============== PRUEBAS Y COMPARACIÓN ==============

def comparar_rendimiento(n, k, spark):
    """Compara rendimiento local y distribuido para matrices de tamaño n y potencia k."""
    A = generar_matriz_simetrica(n)
    resultado_local, tiempo_local = medir_rendimiento_local(A, k)
    resultado_distribuido, tiempo_distribuido = medir_rendimiento_distribuido(spark, A, k)

    print(f"Tamaño matriz: {n}x{n}, Potencia: {k}")
    print(f"Tiempo Local: {tiempo_local:.6f} s")
    print(f"Tiempo Distribuido: {tiempo_distribuido:.6f} s\n")

# ============== CONFIGURACIÓN Y EJECUCIÓN ==============

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("CompararRendimientoMatrices") \
        .getOrCreate()

    configuraciones = [
        (5, 10), (10, 50), (20, 100), (50, 200), (100, 500),
        (200, 1000), (300, 1500), (500, 2000), (1000, 3000)
    ]

    for n, k in configuraciones:
        comparar_rendimiento(n, k, spark)

    spark.stop()
