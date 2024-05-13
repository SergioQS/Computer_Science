""" Escriba una función que, dados tres números l, r y k, 
retorne cuántos números entre l y r (inclusive) son divisibles por k. """

def num_div_between(l,r,k):
    count = 0
    for i in range(l,r+1):
        if i % k == 0:
            count += 1
    return count
#print(num_div_between(6,11,3))
#print(num_div_between(6,20,3))


"""Escriba una función que calcule el factorial de un número."""
def factorial(n):
    fact = 1
    if n > 1:
        fact = factorial(n-1) * n 
    return fact

#print(factorial(3))


"""Construya una función que calcule el doble factorial de un número:
https://es.wikipedia.org/wiki/Doble_factorial"""

def doble_factorial(n):
    fact = 1
    if n > 1:
        fact = doble_factorial(n-2) * n 
    return fact
 
#print(doble_factorial(9))  # 9!! = 945 ,  n!! = 2^k * k!


"""Escriba una función que, dado un n y k, calcule el coeficiente binomial """

def coeficiente_binomial(n,k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))
coeficiente_binomial(12,5) # 792


""" calcular si un numero es primo o no, retornar un booleano """
def primo(n):
    flag  = True
    for i in range(2,(n//2)+1):
        if n % i == 0:
            flag = False
    return flag

primo(3)
primo(7)
primo(997) 
# ahora algunos no primos:
primo(57)
primo(49)

""" Haga una función que determine cuántos primos hay en un rango de números."""

def primos_entre(n,m):
    c = 0
    for i in range(n,m+1):
        if primo(i):
            c += 1
    return c

#primos_entre(2,19)
#primos_entre(16,20)

# primos fuertes 

"""Escriba una función que dado un número m de términos, 
aproxime la evaluación de la función seno en un punto x, 
usando la serie de Taylor:"""

def aprox_seno(p,m):
    sen = 0
    for i in range(0,m+1):
        sen += (((-1)**i)*(p**(2*i+1)))/factorial((2*i + 1))
    return sen

#print("True: sen(1)= ",aprox_seno(1,200))
#print("True: sen(2)= ",aprox_seno(2,200))
#print("True: sen(3)= ",aprox_seno(3,200))

#print("false: sen(40)= ",aprox_seno(40,200)) # acá la serie de taylor ya no aproxima bien (al estar centrada en 0)

"""Escriba una función en C/C++ que determine el área y el volumen de un cono truncado.
Estos valores deben ser actualizados en los argumentos pasados por referencia."""

"""Calcule los números de Catalan de un número utilizando la definición recursiva."""

#C_0 = 1, C_n = sum_i=1 ^ n  C_i-1 C_n-i

def catalan(n):
    if n>0:
        return int((2*(2*n-1)/(n+1))*catalan(n-1))
    return 1
    
#print("El tercer número de Catalan es: ", )

#for i in range(1,10):
#    print("el", i,"ésimo numero de catalán es: ", catalan(i))


""" Escriba una función que encuentre el n-ésimo término de la secuencia de 
Fibonacci utilizando recursión"""

def n_fibo(n):
  if n==1 or n==0:
    return n
  return n_fibo(n-1)+n_fibo(n-2)

#print("el numero de fib en la posición dada 3es: ", n_fibo(int(input("posición: "))))

#for i in range(1,10):
#    print("el", i,"ésimo numero de fib es: ", n_fibo(i))


"""Imprima los 100 primeros números naturales utilizando recursión."""


def imprimir_naturales(n):
    print(n-1)
    if n > 1:
        imprimir_naturales(n-1)
    return None
#imprimir_naturales(10)

""" Función para crear una lista de tamaño n con los valores introducidos"""

def crear_lista():
    Lista = []
    n = int(input("Tamaño de la lista: "))
    for i in range(0,n):
        Lista.append((input("inserte un termino para la lista: ")))

    return Lista



""" Encontrar la cantidad de numeros positivos en una lista de manera recursiva """

def num_positivos(lista,p,r):
    
    if p == r:
        if lista[p] >= 0:
            return 1
        if lista[p] < 0:
            return 0
    q = ((p+r)//2) 
    suma = num_positivos(lista,p,q)
    suma += num_positivos(lista,q+1,r)
    return suma
    

#print(num_positivos([1,-3,2,3,-2,-1,4,5],0,7))
#print(num_positivos([1,-3,0,4,-2,-1,5,6],0,7))



""" Multiplicar dos matrices A,B de tamaño nxn """

def matriz_mult(A,B,n):
    C = []
    for m in range(4):
        C.append([])
    for l in range(4):
        for k in range(4):
            C[l].append(0)

    for fila in range(n):
        for columna in range(n):
            sum = 0
            for k in range(n):
                sum += A[fila][columna]*B[columna][k]
            C[fila][columna] = sum
    return C
#print(matriz_mult(A,B,4))


def matriz_mult_dec(A,B,n):
    C = [ [0 for i in range(n)] for j in range(n)]

    for fila in range(n):
        for columna in range(n):
            sum = 0
            for k in range(n):
                sum += A[fila][columna]*B[columna][k]
            C[fila][columna] = sum
    return C


A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#print(matriz_mult_dec(A,B,4))

# Funciones para matrices de unos, ceros, identidad de nxn:

def unos(n):
    C = []
    for m in range(4):
        C.append([])
    for l in range(4):
        for k in range(4):
            C[l].append(1)
    return C

def ceros(n):
    C = []
    for m in range(4):
        C.append([])
    for l in range(4):
        for k in range(4):
            C[l].append(0)
    return C

def identidad(n):
    C = []
    for m in range(4):
        C.append([])
    for l in range(4):
        for k in range(4):
            C[l].append(0)
            if l == k:
                C[l][k] = 1
    return C
# print(identidad(4))

""" De forma declarativa: """
def ceros_dec(n):
    return [ [0 for i in range(n)] for j in range(n)]
#print(ceros_dec(4))

def unos_dec(n):
    return [ [1 for i in range(n)] for j in range(n)]
#print(unos_dec(4))

def identidad_dec(n):
   C = [ [0 for i in range(n)] for j in range(n)]
   for i in range(n):
        C[i][i] = 1 
   return C
#print(identidad_dec(4))