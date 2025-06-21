#Ejercicio resuelto:
# Este programa simple tiene como objetivo imprimir los números del 1 al 10.
# Es un ejemplo clásico para introducir el concepto de bucles o ciclos.

# La palabra clave 'for' se usa para iniciar un bucle que iterará sobre una secuencia.
# 'i' es la variable de control del bucle. En cada "vuelta" del bucle,
# 'i' tomará un valor diferente de la secuencia que le indiquemos.

# 'range(1, 11)' genera una secuencia de números.
# - El primer número (1) es el INICIO de la secuencia (incluido).
# - El segundo número (11) es el FINAL de la secuencia (excluido).
# Esto significa que la secuencia generada será 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

for i in range(1, 11):
    # 'print(i)' es la acción que se ejecuta en cada repetición del bucle.
    # Imprime el valor actual de la variable 'i' en la consola.
    # Cada número se imprimirá en una nueva línea por defecto.
    print(i)

# Cuando el bucle termina, es decir, cuando 'i' ha tomado todos los valores de la secuencia
# generada por 'range(1, 11)', el programa continúa con la siguiente instrucción
# después del bucle (o finaliza si no hay más código).