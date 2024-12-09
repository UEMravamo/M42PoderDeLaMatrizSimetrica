def multiplicar_matrices(m1, m2):
  """Multiplica dos matrices cuadradas."""
  n = len(m1)  # Dimensión de la matriz

  # Crea una matriz de dimensión n llena de ceros
  resultado = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        # Vamos llenando la matriz resultado
        # Recordamos que las multiplicaciones de matrices son FILAS x COLUMNAS
        resultado[i][j] += m1[i][k] * m2[k][j]
  return resultado


def elevar_matriz_a_potencia(a, k):
  """Eleva una matriz cuadrada a una potencia k."""
  n = len(a)  # Dimensión de la matriz

  # Matriz identidad de la dimensión de la matriz original
  identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

  resultado = identidad

  for _ in range(k):  # Repite k veces
    resultado = multiplicar_matrices(resultado, a)
  return resultado


# Matriz A
A = [
  [2, 1, -1],
  [1, 0, 1],
  [-1, 1, 2]
]
k = 4

# Calcular A elevado a k
Ak = elevar_matriz_a_potencia(A, k)

# Imprimir el resultado
print("Matriz A^4:")
for fila in Ak:
  print(fila)
