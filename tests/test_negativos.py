import numpy as np
import time
from tests.num_negativos import generador_matrices, generador_matrices_negativas, exponenciacion_binaria


def test_exponenciacion_binaria_matrices_negativas():
    """
    Verifica que la exponenciación binaria funcione correctamente con matrices generadas 
    por generador_matrices_negativas.
    """
    size_matriz = 5
    potencia = 100  # Exponente alto
    A = generador_matrices_negativas(size_matriz)

    result = exponenciacion_binaria(A, potencia)
    expected_result = np.round(np.linalg.matrix_power(A, potencia), 2)
    # comprobamos  si los resultados son similares
    if np.allclose(result, expected_result, atol=1e-3):
        print("Resultado para matrices negativas: Superado")
    else:
        print("Resultado para matrices negativas: Fallido")
        print("Resutado esperado:")
        print(expected_result)
        print("Resultado que nos ha dado:")
        print(result)


def test_exponenciacion_binaria_comparar_rendimiento():
    """
    Compara el rendimiento entre matrices generadas por generador_matrices y 
    generador_matrices_negativas, y verifica que los resultados son consistentes.
    """
    size_matriz = 100
    potencia = 100

    # Matrices generadas por generador_matrices
    ini = time.time()
    A1 = generador_matrices(size_matriz)
    result1 = exponenciacion_binaria(A1, potencia)
    time_generador_matrices = time.time() - ini
    print("Matriz generada por generador_matrices:")
    print(A1)

    # Matrices generadas por generador_matrices_negativas
    ini = time.time()
    A2 = generador_matrices_negativas(size_matriz)
    result2 = exponenciacion_binaria(A2, potencia)
    time_generador_matrices_negativas = time.time() - ini
    print("Matriz generada por generador_matrices_negativas:")
    print(A2)

    # Verificar que los resultados son válidos
    expected_result1 = np.round(np.linalg.matrix_power(A1, potencia), 2)
    expected_result2 = np.round(np.linalg.matrix_power(A2, potencia), 2)

    if not np.allclose(result1, expected_result1, atol=1e-3):
        print("Resultado para matrices simetricas: Fallido")
        print("Resultado esperado:")
        print(expected_result1)
        print("Resultado que nos ha dado:")
        print(result1)
    else:
        print("Resultado para matrices simetricas: Superado")

    if not np.allclose(result2, expected_result2, atol=1e-3):
        print("Resultado para matrices negativas: Fallido")
        print("Resutado esperado:")
        print(expected_result2)
        print("Resultado que nos ha dado:")
        print(result2)
    else:
        print("Resultado para matrices negativas: Superado")

    # imprimimos los  tiempos de ejecucion
    print("Tiempo para generador_matrices:")
    print(f"{time_generador_matrices:.4f} segundos")
    print("Tiempo para generador_matrices_negativas:")
    print(f"{time_generador_matrices_negativas:.4f} segundos")

    # verificamos que los tiempos son razonablemente similares
    if abs(time_generador_matrices - time_generador_matrices_negativas) < 1.0:
        print("Comparación de rendimiento: Superado")
    else:
        print("Comparación de rendimiento: Fallido")
