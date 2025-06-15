# Este programa calcula el promedio (media aritmética) de una cantidad 'N' de números
# que el usuario decide ingresar. Es un buen ejemplo de cómo manejar entradas variables
# y realizar cálculos condicionales.

# 1. Solicitar la cantidad de números:
# Le preguntamos al usuario cuántos números quiere promediar.
# 'input(...)' obtiene la entrada como texto, y 'int(...)' la convierte a un número entero.
cantidad = int(input("¿Cuántos números deseas ingresar para calcular el promedio? "))

# 2. Inicializar la variable para la suma:
# 'suma = 0' es donde acumularemos todos los números que el usuario ingrese.
# Siempre empezamos en cero antes de sumar cualquier valor.
suma = 0

# 3. Validar la cantidad ingresada:
# Es crucial verificar si 'cantidad' es mayor que 0.
# No podemos calcular el promedio de cero números (división por cero).
# Si 'cantidad' es 0 o un número negativo, el programa mostrará un mensaje de error.
if cantidad > 0:
    # 4. Bucle para ingresar y sumar los números:
    # Si 'cantidad' es válida, iniciamos un bucle 'for' que se repetirá 'cantidad' veces.
    # 'range(cantidad)' generará números desde 0 hasta 'cantidad - 1'.
    # 'i' será nuestra variable de control, que nos ayuda a saber qué número estamos pidiendo.
    for i in range(cantidad):
        # a. Solicitar cada número:
        # Usamos una f-string 'f"Ingresa el numero {i+1}: "' para mostrar un mensaje amigable
        # que indica qué número estamos pidiendo (ej. "Ingresa el numero 1:", "Ingresa el numero 2:").
        # 'float(...)' convierte la entrada a un número de punto flotante (decimal),
        # lo que permite al usuario ingresar números con decimales para el promedio.
        num = float(input(f"Ingresa el numero {i+1}: "))
        
        # b. Acumular la suma:
        # 'suma += num' añade el número recién ingresado a nuestra variable 'suma'.
        # Esto acumula el total de todos los números.
        suma += num
    
    # 5. Calcular el promedio:
    # Después de que el bucle termina y todos los números han sido sumados,
    # calculamos el promedio dividiendo la 'suma' total por la 'cantidad' de números.
    promedio = suma / cantidad
    
    # 6. Mostrar el resultado:
    # Finalmente, se imprime el promedio calculado usando una f-string para un mensaje claro.
    print(f"El promedio de los {cantidad} números es: {promedio}")
else:
    # Si la 'cantidad' inicial no fue mayor que cero, se ejecuta este bloque.
    # Se informa al usuario que no es posible calcular el promedio con cero números.
    print("No se pueden calcular el promedio de cero números.")