# Este programa determina si un numero entero ingresado por el usuario es un "numero perfecto".

# ¿Que es un numero perfecto?
# Un numero perfecto es un entero positivo que es igual a la suma de sus divisores propios positivos.
# Los divisores propios de un numero son todos sus divisores excepto el propio numero.
# Ejemplos:
# - El numero 6 es perfecto: Sus divisores propios son 1, 2 y 3. Y 1 + 2 + 3 = 6.
# - El numero 28 es perfecto: Sus divisores propios son 1, 2, 4, 7, 14. Y 1 + 2 + 4 + 7 + 14 = 28.

# 1. Solicitar el numero al usuario:
# Pedimos al usuario que ingrese un numero entero.
# 'input(...)' obtiene el texto y 'int(...)' lo convierte a un numero.
num = int(input("Ingresa un numero para saber si es perfecto: "))

# 2. Inicializar la variable para la suma de divisores:
# 'suma_divisores = 0' es donde acumularemos la suma de los divisores propios del numero.
# La inicializamos en 0 porque aun no hemos encontrado ningun divisor.
suma_divisores = 0

# 3. Manejar el caso de numeros no positivos:
# Por definicion, los numeros perfectos son enteros POSITIVOS.
# Si el usuario ingresa un numero menor o igual a 0, informamos que no es perfecto.
if num <= 0:
    print(f"{num} no es un numero perfecto.")
else:
    # 4. Bucle para encontrar y sumar los divisores propios:
    # Este bucle 'for' recorre todos los numeros desde 1 hasta 'num - 1'.
    # Estos son los posibles divisores propios del numero.
    # Por ejemplo, si 'num' es 6, 'i' ira de 1 a 5.
    for i in range(1, num): # Recorremos los posibles divisores propios
        # a. Comprobar si 'i' es un divisor:
        # 'if num % i == 0:' verifica si el resto de la division de 'num' por 'i' es 0.
        # Si es 0, significa que 'i' es un divisor exacto de 'num'.
        if num % i == 0:
            # b. Sumar el divisor encontrado:
            # Si 'i' es un divisor, lo añadimos a nuestra 'suma_divisores'.
            suma_divisores += i
    
    # 5. Comparar la suma de divisores con el numero original:
    # Una vez que el bucle ha terminado de revisar todos los posibles divisores,
    # comparamos la 'suma_divisores' con el 'num' original.
    if suma_divisores == num:
        # Si son iguales, el numero es perfecto.
        print(f"{num} es un numero perfecto.")
    else:
        # Si no son iguales, el numero no es perfecto.
        print(f"{num} no es un numero perfecto.")