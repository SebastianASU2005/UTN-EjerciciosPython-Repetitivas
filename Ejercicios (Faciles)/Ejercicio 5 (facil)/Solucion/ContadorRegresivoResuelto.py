# Este programa imprime una cuenta regresiva, empezando desde el 10 y llegando hasta el 0.
# Es un buen ejemplo para mostrar cómo la función 'range()' puede generar secuencias descendentes.

# La instrucción 'for' inicia un bucle que iterará sobre una serie de números.
# La variable 'i' tomará cada uno de estos números en cada repetición del bucle.

# 'range(10, -1, -1)' es la clave aquí. Esta función genera una secuencia de números:
# - El primer número (10) es el INICIO de la secuencia (inclusive). Este será el primer valor de 'i'.
# - El segundo número (-1) es el FIN de la secuencia (exclusive). Esto significa que el bucle
#   se detendrá antes de llegar a -1, por lo tanto, el 0 será el último número que 'i' tomará.
# - El tercer número (-1) es el PASO. Indica que 'i' disminuirá de 1 en 1 en cada iteración.
#   Un paso negativo es lo que hace que la cuenta sea regresiva.

for i in range(10, -1, -1):
    # En cada "vuelta" del bucle, 'print(i)' mostrará el valor actual de 'i'.
    # Los valores que se imprimirán serán: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.
    print(i)

# Una vez que 'i' ha recorrido todos los números de la secuencia generada por 'range()',
# el bucle finaliza y el programa termina.