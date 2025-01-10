import numpy as np

def diagonalize_and_exponentiate(matrix, power):
    """
    Básicamente, este método descompone la matriz en partes más fáciles de manejar y luego las vuelve a unir.
    Esto lo hacemos porque así elevamos los valores propios a la potencia de forma directa,
    lo que nos ahorra mucho trabajo comparado con multiplicar la matriz muchas veces.
    """

    def is_symmetric(mat):
        # Aquí chequeamos si la matriz es simétrica (si es igual a su traspuesta).
        return np.allclose(mat, mat.T)

    if not is_symmetric(matrix):
        raise ValueError("Hey, la matriz que metiste no es simétrica. Asegúrate de eso antes de seguir.")

  
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)

    diag_power = np.diag(eigenvalues ** power)

    result = eigenvectors @ diag_power @ eigenvectors.T

    return np.round(result, 2)

def main():
    # Aquí definimos una matriz simétrica como ejemplo.
    n = 3  # Dimensión de la matriz
    matrix = np.array([
        [2, 1, -1],
        [1, 0, -1],
        [-1, -1, 2]
    ])
    power = 4  # Exponente que queremos usar

    print("Matriz original:")
    print(matrix)

    # Aquí llamamos al método para calcular la potencia de la matriz.
    result = diagonalize_and_exponentiate(matrix, power)

    print(f"Matriz elevada a la potencia {power}:")
    print(result)

if __name__ == "__main__":
    main()

"""
Paso 1: Descomponemos la matriz en valores propios y vectores propios. 
Esto significa que estamos dividiendo la matriz en partes más simples. 
Paso 2: Elevamos los valores propios (que están en forma diagonal) a la potencia deseada. 
Es mucho más sencillo elevar números que multiplicar matrices grandes repetidamente. d
Redondeamos el resultado a 2 decimales porque queremos que sea bonito y fácil de leer.
Paso 3: Reconstruimos la matriz utilizando 
los vectores propios y los valores elevados. 
Esto nos permite obtener la matriz original elevada a la potencia sin tanto esfuerzo.
   """