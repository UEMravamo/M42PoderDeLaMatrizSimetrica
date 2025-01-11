# para comparar tiempos
import timeit
import numpy as np
# importamos las funciones de los scripts_descartados que vamos a comparar en tiempo
from test_sin_numpy_exponenciacion_rapida import elevar_matriz_a_potencia_exponenciacion_rapida
from exponenciacion_binaria import exponenciacion_binaria


# Matriz con nums de tres cifras 3 * 3 sencilla
matriz = [
    [123, 456, 789],
    [234, 567, 890],
    [345, 678, 901],
]

# Parámetros de la prueba
potencia = 5

# Función para medir el tiempo de elevar_matriz_a_potencia_exponenciacion_rapida


def medir_tiempo_exponenciacion_rapida():
    elevar_matriz_a_potencia_exponenciacion_rapida(matriz, potencia)

# Función para medir el tiempo de exponenciacion_binaria


def medir_tiempo_exponenciacion_binaria():
    exponenciacion_binaria(np.array(matriz), potencia)


# Número de repeticiones para medir el tiempo
repeticiones = 100

# cada tiempo
tiempo_rapida = timeit.timeit(
    medir_tiempo_exponenciacion_rapida, number=repeticiones)
tiempo_binaria = timeit.timeit(
    medir_tiempo_exponenciacion_binaria, number=repeticiones)
print(f"Tiempo de exponenciación rápida (sin NumPy): {
      tiempo_rapida:.6f} segundos")
print(f"Tiempo de exponenciación binaria (con NumPy): {
      tiempo_binaria:.6f} segundos")
