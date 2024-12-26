#test Adrian: 22004996

import pytest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts_descartados.sin_numpy_exponenciacion_rapida import elevar_matriz_a_potencia_exponenciacion_rapida, multiplicar_matrices



@pytest.fixture
def matriz_cuadrada_tres_cifras():
    """
    Genera una matriz cuadrada con números de tres cifras.

    Returns:
        list of list of int: Matriz cuadrada con números de tres cifras.
    """
    return [
        [123, 456, 789],
        [234, 567, 890],
        [345, 678, 901],
    ]


def test_multiplicar_matrices(matriz_cuadrada_tres_cifras):
    """
    Verifica que la multiplicación de matrices con números de tres cifras funciona correctamente.
    """
    # Multiplica la matriz por sí misma.
    resultado = multiplicar_matrices(matriz_cuadrada_tres_cifras, matriz_cuadrada_tres_cifras)
    # Calcula el resultado esperado usando numpy.
    esperado = np.dot(matriz_cuadrada_tres_cifras, matriz_cuadrada_tres_cifras).tolist()
    # Compara los resultados.
    assert resultado == esperado


def test_elevacion_exponenciacion_rapida(matriz_cuadrada_tres_cifras):
    """
    Verifica que la función de exponenciación rápida produce el resultado esperado con números de tres cifras.
    """
    k = 3  # Potencia
    # Calcula la potencia de la matriz usando la implementación.
    resultado = elevar_matriz_a_potencia_exponenciacion_rapida(matriz_cuadrada_tres_cifras, k)
    # Calcula el resultado esperado usando numpy.
    esperado = np.linalg.matrix_power(np.array(matriz_cuadrada_tres_cifras), k).tolist()
    # Compara los resultados.
    assert np.allclose(resultado, esperado, atol=1e-3)


def test_matriz_identidad_tres_cifras(matriz_cuadrada_tres_cifras):
    """
    Verifica que la exponenciación rápida devuelve la matriz identidad
    cuando la potencia es 0 con números de tres cifras.
    """
    k = 0
    # Calcula la matriz a la potencia 0.
    resultado = elevar_matriz_a_potencia_exponenciacion_rapida(matriz_cuadrada_tres_cifras, k)
    # Genera la matriz identidad esperada.
    identidad = np.eye(len(matriz_cuadrada_tres_cifras), dtype=int).tolist()
    # Compara los resultados.
    assert resultado == identidad
