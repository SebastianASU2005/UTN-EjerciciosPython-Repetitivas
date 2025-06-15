# Este programa le pide al usuario un número y luego muestra la tabla de multiplicar de ese número
# desde el 1 hasta el 10. Es un excelente ejemplo del uso del bucle 'for' para tareas repetitivas.

# 1. Solicitar la entrada del usuario:
# 'input("...")' muestra un mensaje al usuario para que ingrese un valor.
# 'int(...)' convierte el texto que el usuario ingresa en un número entero,
# ya que necesitamos operar matemáticamente con él.
num = int(input("Ingresa un numero para ver su tabla de multiplicar: "))

# 2. Iniciar el bucle 'for':
# El bucle 'for' se usará para repetir la acción de imprimir 10 veces,
# una vez por cada multiplicador (del 1 al 10).
# 'i' es la variable que tomará cada valor en la secuencia.

# 'range(1, 11)' genera una secuencia de números enteros: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
# - El primer número (1) es el inicio de la secuencia (inclusive).
# - El segundo número (11) es el final de la secuencia (exclusive), lo que significa que el 10 es el último número.
for i in range(1, 11):
    # 3. Imprimir cada línea de la tabla:
    # 'print(f"...")' utiliza una f-string (cadena formateada), que es una forma muy cómoda
    # de insertar el valor de variables directamente dentro de un texto.
    # Dentro de las llaves {} se colocan las variables que queremos mostrar.
    # - '{num}' mostrará el número que el usuario ingresó (ej. 5).
    # - '{i}' mostrará el multiplicador actual en cada iteración del bucle (ej. 1, luego 2, etc.).
    # - '{num * i}' realizará la operación de multiplicación y mostrará el resultado.
    #
    # Por ejemplo, en la primera iteración (cuando i es 1), imprimirá: "5 x 1 = 5"
    # En la segunda iteración (cuando i es 2), imprimirá: "5 x 2 = 10"
    # Y así sucesivamente hasta que 'i' sea 10.
    print(f"{num} x {i} = {num * i}")

# Una vez que el bucle ha recorrido todos los números de 1 a 10,
# el programa finaliza su ejecución.