# Este programa está diseñado para mostrar todos los números pares en un rango específico,
# desde 0 hasta 20, ambos incluidos. Es una forma concisa de usar 'range()' con un paso.

# La instrucción 'for' inicia un bucle que recorrerá una secuencia de números.
# La variable 'i' tomará cada valor de esa secuencia en cada "vuelta" del bucle.

# 'range(0, 21, 2)' es la clave aquí. Esta función genera una secuencia de números:
# - El primer número (0) es el INICIO de la secuencia (inclusive).
# - El segundo número (21) es el FIN de la secuencia (exclusive), lo que significa
#   que el último número generado será 20 (el número antes de 21).
# - El tercer número (2) es el PASO. Esto indica que 'i' no aumentará de 1 en 1,
#   sino de 2 en 2.

for i in range(0, 21, 2):
    # En cada iteración, 'print(i)' mostrará el valor actual de 'i'.
    # Debido a que 'range' está generando números de 2 en 2, 'i' siempre será un número par.
    # Los valores que imprimirá 'i' serán: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
    print(i)

# Una vez que 'i' ha tomado todos los valores de la secuencia generada por 'range()',
# el bucle termina y el programa finaliza.