# Este programa calcula el Maximo Comun Divisor (MCD) de dos numeros enteros
# ingresados por el usuario. Utiliza el algoritmo de Euclides, que es un metodo
# eficiente para encontrar el MCD.

# ¿Que es el MCD? Es el numero mas grande que divide exactamente a dos o mas numeros.
# Por ejemplo, el MCD de 12 y 18 es 6, porque 6 divide tanto a 12 como a 18,
# y no hay un numero mas grande que haga lo mismo.

# 1. Solicitar los numeros al usuario:
# Pedimos al usuario que ingrese dos numeros.
# 'input(...)' obtiene la entrada como texto, y 'int(...)' la convierte a entero.
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

# 2. Preparar los numeros para el algoritmo:
# 'a = abs(num1)' y 'b = abs(num2)'
# Usamos 'abs()' (valor absoluto) para asegurarnos de que trabajamos con numeros positivos.
# El MCD es siempre positivo, sin importar si los numeros originales son negativos.
a = abs(num1)
b = abs(num2)

# 3. Explicacion del algoritmo de Euclides:
# El algoritmo de Euclides se basa en la propiedad de que el MCD de dos numeros
# no cambia si el numero mayor se reemplaza por la diferencia entre ambos numeros.
# Una version mas eficiente de este algoritmo usa el resto de la division.
# La regla es: MCD(a, b) = MCD(b, a % b).
# El proceso se repite hasta que el segundo numero (b) se convierte en 0.
# Cuando 'b' es 0, el valor actual de 'a' sera el MCD.

# 4. El bucle 'while' del algoritmo de Euclides:
# Este bucle continuara ejecutandose MIENTRAS 'b' no sea igual a 0.
while b != 0:
    # a. Guardar el valor actual de 'b':
    # 'temp_b = b' es una variable temporal. La necesitamos porque el valor de 'b'
    # va a cambiar en la siguiente linea, pero necesitamos su valor original
    # para asignarselo a 'a' al final de esta iteracion.
    temp_b = b
    
    # b. Calcular el nuevo 'b':
    # 'b = a % b' calcula el resto de la division de 'a' entre 'b'.
    # Este resto se convierte en el nuevo valor de 'b'.
    # Si b fuera 0 aqui, el bucle terminaria en la proxima comprobacion.
    b = a % b  
    
    # c. Actualizar 'a':
    # 'a = temp_b' asigna el valor antiguo de 'b' (guardado en 'temp_b') a 'a'.
    # Esto "mueve" el valor del anterior 'b' a la posicion del anterior 'a'.
    a = temp_b 
    
# 5. Mostrar el resultado final:
# Una vez que el bucle 'while' termina (es decir, 'b' es 0),
# la variable 'a' contiene el Maximo Comun Divisor.
# Imprimimos el resultado usando una f-string, haciendo referencia a los numeros originales.
print(f"El Maximo Comun Divisor de {num1} y {num2} es: {a}")

# Ejemplo de como funciona el bucle para MCD(48, 18):
# Inicio: a=48, b=18
# 1ra iteracion:
#   temp_b = 18
#   b = 48 % 18 = 12
#   a = 18
#   Ahora: a=18, b=12
# 2da iteracion:
#   temp_b = 12
#   b = 18 % 12 = 6
#   a = 12
#   Ahora: a=12, b=6
# 3ra iteracion:
#   temp_b = 6
#   b = 12 % 6 = 0
#   a = 6
#   Ahora: a=6, b=0
# El bucle termina porque b es 0. El MCD es 6.