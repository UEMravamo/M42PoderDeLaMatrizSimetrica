def mult_matrices(A,B ,n): #Para cada elemento en la matriz C, calcula la suma de los productos de las filas de A y las columnas de B.
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            suma = 0
            for k in range(n):
                suma= suma+A[i][k]* B[k][j]
            C[i][j] = suma
    return C

def simplificar_exponente(A,k,n):
    if k ==0:#si elevas una matriz a 0 da la identidad
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    elif k ==1:#si elevas una matriz a 1 ppues obtienes la misma
        return A
    elif k %2 == 0:#si k(exponente) es par
        parte = simplificar_exponente(A, k//2,n)
        return mult_matrices(parte,parte, n)
    else:#si k(exponente) es impar
        return mult_matrices(A,  simplificar_exponente(A,k-1,n),n)
# Ejemplo A^5, pues se haria la simplificacion del exponente A^5->A^1*A^4->(A^2*A^2)*A^1
# Es decir, si k es par se calcula  A^^k/2 * A^k/2. Y si es impar A * A^k-1


A = [[1, 2,3], #Matriz simetrica
     [2, 5, 0], 
     [3, 0,  5]]

n = len(A)#filas de A
k = int(input("Dime el exponente:"))#hay que ingresar el exponente
#printeamos A
print("A:")
for row in A:
    print(row)

result = simplificar_exponente(A, k, n)
#printeamos el resultado
print(f"A elevado a {k}:")
for row in result:
    print(row)
