import numpy as np

n = 3
k = 16

A = np.array([[2, 1, -1],
              [-1, 0, 1],
              [-1, -1, 2]])

exp = []


def recursivo(exponente):
    exp.insert(0, exponente)
    if exponente == 0:
        return 1
    elif exponente == 1:
        return A
    else:
        return recursivo(exponente // 2)


recursivo(16)

for n in exp:
    if n == 1:
        continue
    A = np.dot(A, A)

print(A)
