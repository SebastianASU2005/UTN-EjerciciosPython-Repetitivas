# Este programa dibuja una pirámide de asteriscos en la consola.
# El tamaño de la pirámide (cuantas filas tendra) es especificado por el usuario.
# Es un excelente ejercicio para entender como combinar bucles y el manejo de cadenas
# para crear patrones visuales.

# 1. Solicitar el numero de filas:
# Pedimos al usuario cuantas filas tendra la piramide.
# 'input(...)' obtiene el texto y 'int(...)' lo convierte a un numero entero.
filas = int(input("Ingresa el numero de filas para la pirámide: "))

# 2. Bucle principal para cada fila de la piramide:
# 'for i in range(1, filas + 1):'
# Este bucle se repetira una vez por cada fila de la piramide.
# 'i' representara el numero de la fila actual, empezando en 1.
# Por ejemplo, si 'filas' es 4, 'i' tomara los valores 1, 2, 3, 4.
for i in range(1, filas + 1):
    # 3. Imprimir espacios en blanco (para centrar la piramide):
    # 'print(" " * (filas - i), end="")'
    # Esta linea calcula y imprime la cantidad necesaria de espacios en blanco
    # ANTES de los asteriscos en cada fila.
    # - 'filas - i': A medida que 'i' aumenta (bajamos de fila), la cantidad de espacios disminuye.
    #   Ejemplo con 'filas = 4':
    #   - i=1 (fila 1): 4 - 1 = 3 espacios
    #   - i=2 (fila 2): 4 - 2 = 2 espacios
    #   - i=3 (fila 3): 4 - 3 = 1 espacio
    #   - i=4 (fila 4): 4 - 4 = 0 espacios
    # - '" " * (cantidad)': Multiplica la cadena de un espacio por el numero calculado,
    #   generando la cantidad correcta de espacios.
    # - 'end=""': Esto es crucial. Normalmente, 'print()' añade un salto de linea al final.
    #   Al usar 'end=""', le decimos a Python que NO añada un salto de linea,
    #   asi los asteriscos se imprimiran en la misma linea despues de los espacios.
    print(" " * (filas - i), end="")
    
    # 4. Imprimir asteriscos:
    # 'print("*" * (2 * i - 1))'
    # Esta linea calcula y imprime la cantidad de asteriscos para la fila actual.
    # - '2 * i - 1': Esta formula genera la secuencia de numeros impares: 1, 3, 5, 7, etc.
    #   que es la cantidad de asteriscos necesaria para cada fila de una piramide centrada.
    #   Ejemplo con 'filas = 4':
    #   - i=1 (fila 1): 2 * 1 - 1 = 1 asterisco
    #   - i=2 (fila 2): 2 * 2 - 1 = 3 asteriscos
    #   - i=3 (fila 3): 2 * 3 - 1 = 5 asteriscos
    #   - i=4 (fila 4): 2 * 4 - 1 = 7 asteriscos
    # - '"*" * (cantidad)': Multiplica la cadena de un asterisco por el numero calculado.
    # Como esta es la ultima parte de la linea, 'print()' añadira un salto de linea por defecto,
    # lo que hara que la proxima fila comience en una nueva linea.
    print("*" * (2 * i - 1))

# Ejemplo de salida para 4 filas:
#    (3 espacios) * (1 asterisco)
#   (2 espacios) *** (3 asteriscos)
#  (1 espacio) ***** (5 asteriscos)
# (0 espacios) ******* (7 asteriscos)