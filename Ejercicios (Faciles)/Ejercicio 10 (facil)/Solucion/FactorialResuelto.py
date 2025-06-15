# Este programa calcula el factorial de un número específico.
# El factorial de un número entero positivo 'n' (representado como n!)
# es el producto de todos los enteros positivos desde 1 hasta 'n'.
# Por ejemplo, el factorial de 5 (5!) es 5 * 4 * 3 * 2 * 1 = 120.

# 1. Definir el número para calcular el factorial:
# En este ejemplo, el número está fijo en 5.
# Podrias pedirselo al usuario con: numero = int(input("Ingresa un numero para calcular su factorial: "))
numero = 5

# 2. Inicializar la variable 'factorial':
# 'factorial = 1' crea una variable para almacenar el resultado del cálculo.
# Se inicializa en 1, no en 0, porque el factorial es un producto.
# Multiplicar por 0 siempre daria 0, lo cual es incorrecto para el factorial.
# Ademas, el factorial de 0 es 1 (0! = 1).
factorial = 1

# 3. Bucle 'for' para calcular el factorial:
# El bucle recorrerá los números desde 1 hasta 'numero' (inclusive).
# 'range(1, numero + 1)' genera la secuencia: 1, 2, 3, 4, 5 (si 'numero' es 5).
# 'i' tomara cada uno de esos valores en cada repeticion.
for i in range(1, numero + 1):
    # En cada iteracion, 'factorial *= i' es una forma corta de 'factorial = factorial * i'.
    # Esto multiplica el valor actual de 'factorial' por 'i', acumulando el producto.
    #
    # Si 'numero' es 5, el proceso seria:
    # - i=1: factorial = 1 * 1 = 1
    # - i=2: factorial = 1 * 2 = 2
    # - i=3: factorial = 2 * 3 = 6
    # - i=4: factorial = 6 * 4 = 24
    # - i=5: factorial = 24 * 5 = 120
    factorial *= i

# 4. Mostrar el resultado:
# Una vez que el bucle ha terminado de multiplicar todos los numeros,
# se imprime el resultado final utilizando una f-string.
print(f"El factorial de {numero} es: {factorial}")