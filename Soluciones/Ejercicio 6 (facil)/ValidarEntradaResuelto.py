# Este programa se asegura de que el usuario ingrese un número que sea positivo (mayor que cero).
# Repetirá la solicitud hasta que se cumpla esa condición, lo que lo hace un buen ejemplo
# de cómo usar un bucle 'while' para la validación de datos.

# 1. Inicializar la variable 'num':
# Asignamos a 'num' un valor inicial de -1.
# Hacemos esto para garantizar que la condición del bucle 'while' (num <= 0)
# sea verdadera al menos una vez y el bucle se ejecute por primera vez.
# Si la inicializáramos en un número positivo, el bucle no se ejecutaría.
num = -1

# 2. El bucle 'while' para la validación:
# Este bucle se repetirá MIENTRAS la condición 'num <= 0' sea verdadera.
# Esto significa que el bucle continuará pidiendo un número mientras 'num'
# sea cero o un número negativo.
while num <= 0:
    # a. Solicitar la entrada al usuario:
    # 'input("...")' muestra el mensaje y espera que el usuario escriba algo.
    # 'int(...)' convierte esa entrada de texto a un número entero.
    num = int(input("Por favor, ingresa un numero positivo: "))
    
    # b. Verificar si la entrada es válida:
    # Este 'if' comprueba si el número ingresado por el usuario NO es positivo.
    # Si 'num' sigue siendo cero o negativo, significa que la entrada es incorrecta.
    if num <= 0:
        # Si la entrada es incorrecta, se imprime un mensaje de error.
        # El bucle 'while' volverá a verificar su condición y, como 'num'
        # sigue siendo <= 0, pedirá el número nuevamente.
        print("Error: El numero debe ser positivo.")

# 3. Mostrar el resultado final:
# Una vez que el bucle 'while' termina (esto solo sucede cuando el usuario
# ingresa un 'num' que es estrictamente mayor que 0),
# se imprime el número válido que finalmente se ingresó.
print(f"numero válido ingresado: {num}")