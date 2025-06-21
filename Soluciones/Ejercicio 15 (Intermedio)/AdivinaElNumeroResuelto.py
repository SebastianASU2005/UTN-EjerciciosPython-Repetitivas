import random # Importamos el modulo 'random' para poder generar numeros aleatorios.

# Este programa es un juego simple donde la computadora elige un numero secreto
# y el usuario tiene que adivinarlo. La computadora da pistas (mas alto o mas bajo)
# hasta que el usuario acierte.

# 1. Generar el numero secreto:
# 'random.randint(1, 100)' genera un numero entero aleatorio entre 1 y 100 (inclusive).
# Este sera el numero que el jugador debe adivinar.
numero_secreto = random.randint(1, 100)

# 2. Inicializar variables para el juego:
# 'intentos = 0' llevara la cuenta de cuantas veces el usuario intenta adivinar.
intentos = 0
# 'adivinado = False' es una bandera booleana. Sera 'True' cuando el usuario adivine el numero,
# y esto hara que el bucle del juego termine.
adivinado = False

# 3. Mensajes de bienvenida al juego:
print("¡Bienvenido al juego de adivinar el numero!")
print("Estoy pensando en un numero entre 1 y 100.")

# 4. El bucle principal del juego:
# 'while not adivinado:' significa "mientras 'adivinado' sea False".
# El juego continuara pidiendo intentos hasta que 'adivinado' se convierta en 'True'.
while not adivinado:
    # 5. Manejo de errores con 'try-except':
    # El bloque 'try' intenta ejecutar el codigo que podria causar un error (como una conversion de texto a numero).
    try:
        # a. Pedir el intento al usuario:
        # 'input("¿Cual es tu intento? ")' solicita al usuario que ingrese un numero.
        # 'int(...)' intenta convertir la entrada del usuario a un numero entero.
        intento = int(input("¿Cual es tu intento? "))
        
        # b. Incrementar el contador de intentos:
        # Sumamos 1 a 'intentos' cada vez que el usuario hace una suposicion.
        intentos += 1
        
        # c. Dar pistas al usuario:
        # Comparamos el 'intento' del usuario con el 'numero_secreto'.
        if intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Intenta de nuevo!")
        else:
            # d. Si el numero es adivinado:
            # Si el 'intento' es igual al 'numero_secreto', el usuario gano.
            # Cambiamos 'adivinado' a 'True' para que el bucle 'while' termine.
            adivinado = True
            # Imprimimos un mensaje de felicitacion mostrando el numero y la cantidad de intentos.
            print(f"¡Felicidades! Adivinaste el numero {numero_secreto} en {intentos} intentos.")
    
    # 6. Manejar errores de entrada ('ValueError'):
    # Si el usuario ingresa algo que no puede convertirse a un numero entero (ej. "hola"),
    # Python lanzara un 'ValueError'. El bloque 'except ValueError:' captura ese error.
    except ValueError:
        # Se imprime un mensaje amigable para el usuario, pidiendole que ingrese un numero valido.
        print("Por favor, ingresa un numero valido.")
        # El bucle continua, pidiendo un nuevo intento.

# Una vez que 'adivinado' es True, el bucle termina y el programa finaliza.