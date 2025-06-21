# Este es un programa sencillo que le pide al usuario una cantidad
# y luego imprime esa cantidad de asteriscos en una sola línea.
# Es un excelente ejemplo para mostrar la potencia de la multiplicación de strings en Python.

# 1. Solicitar la cantidad de asteriscos:
# 'input("...")' muestra el mensaje "¿Cuantos asteriscos quieres imprimir? "
# y espera que el usuario escriba un número y presione Enter.
# 'int(...)' convierte esa entrada de texto a un número entero, ya que necesitamos
# una cantidad numérica para la operación.
cantidad_asteriscos = int(input("¿Cuantos asteriscos quieres imprimir? "))

# 2. Imprimir los asteriscos:
# Aquí está la magia: Python permite multiplicar una cadena de texto (string) por un número entero.
# Cuando multiplicas un string como "*" por un número (ej. 5),
# el resultado es que el string se repite esa cantidad de veces ("*****").
# 'print(...)' muestra este resultado directamente en la consola.
print("*" * cantidad_asteriscos)

# Por ejemplo, si el usuario ingresa 7, el programa imprimirá: "*******"
# Si ingresa 0, imprimirá una línea vacía.