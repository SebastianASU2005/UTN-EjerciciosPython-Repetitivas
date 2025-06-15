# Este programa genera e imprime los primeros 'n' términos de la secuencia de Fibonacci.
# La secuencia de Fibonacci es una serie donde cada número es la suma de los dos anteriores,
# comenzando con 0 y 1. La secuencia se ve asi: 0, 1, 1, 2, 3, 5, 8, 13, ...

# 1. Solicitar la cantidad de terminos:
# Pedimos al usuario cuantos terminos de la secuencia quiere ver.
# 'input(...)' obtiene la entrada como texto, y 'int(...)' la convierte a un numero entero.
n = int(input("Ingresa la cantidad de terminos de Fibonacci que deseas ver: "))

# 2. Inicializar los primeros dos terminos y el contador:
# La secuencia de Fibonacci siempre comienza con 0 y 1.
# 'a' guarda el primer termino, 'b' guarda el segundo.
a, b = 0, 1
# 'contador' nos ayuda a llevar la cuenta de cuantos terminos hemos generado hasta ahora.
# Empezamos en 0 porque aun no hemos generado ninguno.
contador = 0

# 3. Manejar casos especiales para 'n':
# Es importante considerar que el usuario podria ingresar 0 o un numero negativo,
# o solo querer ver el primer termino.

# Si 'n' es menor o igual a 0:
# No tiene sentido generar una secuencia con cero o menos terminos.
if n <= 0:
    print("Por favor, ingresa un numero entero positivo.")
# Si 'n' es 1:
# Solo necesitamos imprimir el primer termino, que es 0.
elif n == 1:
    print("Secuencia de Fibonacci:")
    print(a) # Imprime el 0
# Si 'n' es mayor que 1 (el caso mas comun):
else:
    print("Secuencia de Fibonacci:")
    # 4. Bucle 'while' para generar la secuencia:
    # Este bucle se ejecutara mientras el 'contador' sea menor que 'n'.
    # Cada vez que el bucle se repite, generamos e imprimimos un nuevo termino.
    while contador < n:
        # a. Imprimir el termino actual:
        # Imprimimos el valor actual de 'a', que es el termino de Fibonacci en esta iteracion.
        print(a)
        
        # b. Calcular el siguiente termino:
        # El siguiente termino de la secuencia es la suma de los dos terminos anteriores ('a' y 'b').
        siguiente = a + b
        
        # c. Actualizar 'a' y 'b' para la proxima iteracion:
        # Para la siguiente iteracion, el 'nuevo a' sera el 'viejo b'.
        # Y el 'nuevo b' sera el 'siguiente' termino que acabamos de calcular.
        # Esto "desplaza" los valores hacia adelante en la secuencia.
        a = b
        b = siguiente
        
        # d. Incrementar el contador:
        # Aumentamos el contador en 1, porque ya hemos generado un termino mas.
        # Esto es crucial para que el bucle 'while' eventualmente termine
        # cuando el 'contador' alcance 'n'.
        contador += 1

# Una vez que el 'contador' es igual a 'n', el bucle 'while' se detiene
# y el programa ha terminado de imprimir la secuencia.