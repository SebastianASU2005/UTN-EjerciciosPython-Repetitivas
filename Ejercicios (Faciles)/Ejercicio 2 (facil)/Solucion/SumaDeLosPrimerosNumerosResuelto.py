# Este programa calcula la suma de todos los números enteros desde 1 hasta un número 'N'
# que el usuario introduce. Por ejemplo, si N es 5, sumará 1 + 2 + 3 + 4 + 5.

# 1. Solicitar la entrada del usuario:
# 'input("...")' muestra un mensaje en la consola y espera que el usuario escriba algo
# y presione Enter. Lo que el usuario escribe siempre se recibe como texto (string).
# 'int(...)' convierte ese texto a un número entero. Es crucial porque necesitamos
# operar matemáticamente con 'N'.
N = int(input("Ingresa un número N para sumar hasta él: "))

# 2. Inicializar variables:
# 'suma' guardará el resultado acumulado. Empezamos en 0 porque aún no hemos sumado nada.
suma = 0
# 'contador' nos ayudará a recorrer los números desde 1 hasta N.
# Empezamos en 1 porque queremos sumar desde el número 1.
contador = 1

# 3. El bucle 'while':
# El bucle 'while' repite un bloque de código MIENTRAS una condición sea verdadera.
# En este caso, el bucle continuará ejecutándose mientras 'contador' sea menor o igual a 'N'.
# Una vez que 'contador' sea mayor que 'N', el bucle se detendrá.
while contador <= N:
    # a. Sumar el número actual:
    # 'suma += contador' es una forma abreviada de 'suma = suma + contador'.
    # En cada repetición, el valor actual de 'contador' se añade a nuestra variable 'suma'.
    suma += contador
    
    # b. Incrementar el contador:
    # 'contador += 1' es lo mismo que 'contador = contador + 1'.
    # Esto es VITAL en un bucle 'while'. Si no incrementamos el contador,
    # la condición 'contador <= N' siempre sería verdadera (si N es positivo)
    # y el bucle se repetiría infinitamente, creando un "bucle infinito".
    contador += 1

# 4. Mostrar el resultado:
# Una vez que el bucle 'while' ha terminado (porque 'contador' ya superó a 'N'),
# significa que hemos sumado todos los números deseados.
# 'print(f"...")' usa una f-string (string formateada) para insertar los valores
# de las variables directamente dentro del texto, haciendo el mensaje más claro.
print(f"La suma de los primeros {N} números es: {suma}")

# ¡Pruébalo! Si ingresas N=3, el proceso sería:
# 1. N = 3, suma = 0, contador = 1
# 2. Bucle: contador (1) <= N (3) es VERDADERO
#    suma = 0 + 1 = 1
#    contador = 1 + 1 = 2
# 3. Bucle: contador (2) <= N (3) es VERDADERO
#    suma = 1 + 2 = 3
#    contador = 2 + 1 = 3
# 4. Bucle: contador (3) <= N (3) es VERDADERO
#    suma = 3 + 3 = 6
#    contador = 3 + 1 = 4
# 5. Bucle: contador (4) <= N (3) es FALSO. El bucle termina.
# 6. Se imprime: "La suma de los primeros 3 números es: 6"