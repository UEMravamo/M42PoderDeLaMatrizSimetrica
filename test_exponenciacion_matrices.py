# Test de Adrian 22004996

import pytest
import numpy as np
from sin_numpy_exponenciacion_rapida import (
    elevar_matriz_a_potencia_exponenciacion_rapida,
    multiplicar_matrices,
)
from exponenciacion_binaria import generador_matrices, exponenciacion_binaria


@pytest.fixture
def matrizCuadradaTresCifras():
    """
    Genera una matriz cuadrada 3x3 con valores de tres cifras.

    Returns:
        list of list of int: Matriz cuadrada con valores fijos.
    """
    return [
        [123, 456, 789],
        [234, 567, 890],
        [345, 678, 901],
    ]


def testMultiplicarMatrices():
    """
    Prueba la multiplicación de dos matrices cuadradas usando la implementación manual.

    Verifica que el resultado sea correcto al compararlo con un resultado esperado.
    """
    # Ejemplo de matrices pequeñas para verificar la funcionalidad básica.
    m1 = [[100, 200], [300, 400]]
    m2 = [[500, 600], [700, 800]]
    # Resultado esperado de la multiplicación.
    resultado = multiplicar_matrices(m1, m2)
    esperado = [
        [190000, 220000],
        [430000, 500000],
    ]
    # Verifica que el resultado coincida con el esperado.
    assert resultado == esperado


def testElevacionExponenciacionRapida(matrizCuadradaTresCifras):
    """
    Prueba la elevación de una matriz a una potencia usando la implementación sin numpy.

    Compara el resultado con el obtenido mediante numpy.linalg.matrix_power.
    """
    k = 3  # Potencia
    # Implementación para calcular la potencia.
    resultado = elevar_matriz_a_potencia_exponenciacion_rapida(
        matrizCuadradaTresCifras, k
    )
    # Calculamos el resultado esperado.
    esperado = np.linalg.matrix_power(
        np.array(matrizCuadradaTresCifras), k
    ).tolist()
    # Verificamos que ambos resultados sean equivalentes.
    assert np.allclose(resultado, esperado, atol=1e-3)


def testGeneradorMatrices():
    """
    Prueba que el generador de matrices simétricas produce matrices válidas.

    Verifica que las matrices generadas son simétricas y tienen las dimensiones correctas.
    """
    N = 3  # Tamaño
    # Generamos la matriz.
    matriz = generador_matrices(N)
    # Verificamos las dimensiones.
    assert matriz.shape == (N, N)
    # Verificamos que sea simétrica (A == A^T).
    assert np.allclose(matriz, matriz.T, atol=1e-3)


def testExponenciacionBinaria(matrizCuadradaTresCifras):
    """
    Prueba la exponenciación binaria usando numpy.

    Compara el resultado con el obtenido mediante numpy.linalg.matrix_power.
    """
    potencia = 3  # Potencia
    matriz = np.array(matrizCuadradaTresCifras)
    resultado = exponenciacion_binaria(matriz, potencia)
    # Calculamos el resultado esperado.
    esperado = np.linalg.matrix_power(matriz, potencia)
    # Verificamos que ambos resultados sean equivalentes.
    assert np.allclose(resultado, esperado, atol=1e-3)


def testComparacionExponenciacionImplementaciones(matrizCuadradaTresCifras):
    """
    Compara las dos implementaciones de elevación de matrices.

    Verifica que la implementación sin numpy y la de exponenciación binaria
    produzcan los mismos resultados.
    """
    potencia = 4  # Potencia
    matriz = matrizCuadradaTresCifras

    # Calculamos el resultado con la implementación sin numpy.
    resultadoRapido = elevar_matriz_a_potencia_exponenciacion_rapida(
        matriz, potencia
    )
    # Calculamos el resultado con exponenciación binaria usando numpy.
    resultadoBinario = exponenciacion_binaria(
        np.array(matriz), potencia
    ).tolist()

    # Comparamos los resultados de ambas implementaciones.
    assert np.allclose(resultadoRapido, resultadoBinario, atol=1e-3)
