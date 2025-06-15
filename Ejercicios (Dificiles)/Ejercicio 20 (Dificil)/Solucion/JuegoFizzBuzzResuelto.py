# Este programa implementa el clasico juego "FizzBuzz".
# El objetivo es imprimir numeros del 1 al 100, pero con algunas reglas especiales:
# - Si el numero es multiplo de 3, imprime "Fizz".
# - Si el numero es multiplo de 5, imprime "Buzz".
# - Si el numero es multiplo de AMBOS (3 y 5), imprime "FizzBuzz".
# - De lo contrario, imprime el numero mismo.

# 1. Bucle principal para recorrer los numeros:
# 'for i in range(1, 101):' crea un bucle que hara que la variable 'i'
# tome cada valor entero desde 1 hasta 100 (incluido).
# 'range(1, 101)' genera la secuencia 1, 2, ..., 100.
for i in range(1, 101):
    # 2. Comprobar la condicion mas especifica primero:
    # 'if i % 3 == 0 and i % 5 == 0:'
    # Esta condicion verifica si el numero 'i' es divisible por 3 Y por 5 al mismo tiempo.
    # El operador '%' (modulo) devuelve el resto de una division.
    # Si 'i % 3 == 0', significa que 'i' es multiplo de 3.
    # Si 'i % 5 == 0', significa que 'i' es multiplo de 5.
    # 'and' significa que AMBAS condiciones deben ser verdaderas.
    # Esta es la condicion mas restrictiva, por lo que la colocamos primero.
    # Si un numero es multiplo de 15 (ej. 15, 30), tambien es multiplo de 3 y 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # 3. Comprobar si es multiplo de 3 (pero no de 5, ya cubierto):
    # 'elif i % 3 == 0:'
    # 'elif' significa "else if" (si no, si...). Solo se comprueba si la condicion 'if' anterior fue falsa.
    # Si el numero 'i' es multiplo de 3 (pero NO es multiplo de 5 tambien, porque ya lo filtramos),
    # entonces imprimimos "Fizz".
    elif i % 3 == 0:
        print("Fizz")
    
    # 4. Comprobar si es multiplo de 5 (pero no de 3, ya cubierto):
    # 'elif i % 5 == 0:'
    # Si las dos condiciones anteriores fueron falsas (no es multiplo de 3 y 5 a la vez, ni solo de 3),
    # ahora verificamos si es multiplo de 5. Si lo es, imprimimos "Buzz".
    elif i % 5 == 0:
        print("Buzz")
    
    # 5. Si ninguna de las condiciones anteriores se cumple:
    # 'else:'
    # Si el numero no es multiplo de 3, ni de 5, ni de ambos,
    # simplemente imprimimos el numero 'i' mismo.
    else:
        print(i)

# El bucle continua hasta que 'i' llega a 100, y luego el programa termina.