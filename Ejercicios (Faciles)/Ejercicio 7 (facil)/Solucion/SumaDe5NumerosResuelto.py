# Este programa le pide al usuario que ingrese 5 números uno por uno
# y luego calcula y muestra la suma total de esos cinco números.

# 1. Inicializar la variable para la suma:
# 'suma = 0' crea una variable llamada 'suma' y le asigna el valor inicial de 0.
# Es importante empezar en 0 porque aún no hemos agregado ningún número.
suma = 0

# 2. Iniciar el bucle 'for':
# 'for i in range(5):' inicia un bucle que se repetirá exactamente 5 veces.
# - 'range(5)' genera una secuencia de números: 0, 1, 2, 3, 4.
# - En cada repeticion, la variable 'i' tomará uno de esos valores.
#   Esto significa que el bucle se ejecutará para i=0, i=1, i=2, i=3, i=4.
for i in range(5):
    # a. Solicitar cada numero al usuario:
    # 'input(f"Ingresa el numero {i+1}: ")' muestra un mensaje al usuario.
    # Usamos '{i+1}' para que el mensaje sea mas amigable, mostrando "Ingresa el numero 1:",
    # luego "Ingresa el numero 2:", y asi sucesivamente.
    # 'int(...)' convierte el texto ingresado por el usuario a un numero entero.
    num = int(input(f"Ingresa el numero {i+1}: "))
    
    # b. Acumular la suma:
    # 'suma += num' es una forma corta de decir 'suma = suma + num'.
    # En cada repeticion del bucle, el numero que el usuario ingresó ('num')
    # se añade a la variable 'suma'. De esta forma, 'suma' va acumulando todos los numeros.
    suma += num

# 3. Mostrar el resultado final:
# Una vez que el bucle ha terminado (despues de pedir y sumar los 5 numeros),
# se imprime el valor final de la variable 'suma' usando una f-string para un mensaje claro.
print(f"La suma de los 5 numeros es: {suma}")