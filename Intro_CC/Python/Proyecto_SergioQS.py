"""
El presente código tiene como fin implementar distintos métodos de multiplicación de matrices y evaluar su eficiencia. """


# Primer Método: Naive. Método clásico de multiplicación de matrices.

#La complejidad del metodo es O(n³) 

def matriz_mult(A,B,n):
    C = [ [0 for i in range(n)] for j in range(n)]

    for fila in range(n):
        for columna in range(n):
            sum = 0
            for k in range(n):
                sum += A[fila][columna]*B[columna][k]
            C[fila][columna] = sum
    return C


# Segundo método: Dividir y conquistar (usando recursividad) Para matrices de ramaño 2**k

#La complejidad es: 

#función para dividir matriz en 4 submatrices,(asumiendo que tiene filas y columnas pares)
def partir(A,n):
    A_11 = []
    A_21 = []
    A_12 = []
    A_22 = []
    for i in range(n/2):
        A_11[j].append([])
        A_21[j].append([])
        A_12[j].append([])
        A_22[j].append([])
        for j in range(n/2):
            A_11[j].append(A[i][j])
            A_21[j].append(A[i+n/2][j])
            A_12[j].append(0[i][j+n/2])
            A_22[j].append(0[i+n/2][j+n/2])

    return A_11, A_21, A_12, A_22

print(partir([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))

def matrix_mult_recursive(A,B,n):
    C = [ [0 for i in range(n)] for j in range(n)]
    if n == 1:
        C[1][1] = A[1][1]
    else:
    #    partir(B)


# Tercer método: Strassen 



