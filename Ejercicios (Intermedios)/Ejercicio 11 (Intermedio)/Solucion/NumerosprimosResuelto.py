# Este programa determina si un numero entero ingresado por el usuario es un numero primo.
# Un numero primo es un numero natural mayor que 1 que tiene unicamente dos divisores positivos distintos:
# el mismo y el 1. Ejemplos: 2, 3, 5, 7, 11, etc.

# 1. Solicitar el numero al usuario:
# 'input(...)' pide al usuario que ingrese un numero.
# 'int(...)' convierte la entrada (que es texto) a un numero entero.
num = int(input("Ingresa un numero para saber si es primo: "))

# 2. Inicializar la bandera 'es_primo':
# 'es_primo' es una variable booleana (True/False) que usaremos como una "bandera" o "indicador".
# Inicialmente, asumimos que el numero ES primo (True) y luego, si encontramos un divisor,
# cambiaremos esta bandera a False.
es_primo = True

# 3. Manejar casos especiales para numeros no primos:
# Por definicion, los numeros menores o iguales a 1 NO son primos.
# Si 'num' es 1 o menos, inmediatamente sabemos que no es primo y establecemos 'es_primo' a False.
if num <= 1:
    es_primo = False
else:
    # 4. Bucle para verificar divisores:
    # Si el numero es mayor que 1, necesitamos buscar posibles divisores.
    # Recorremos los numeros desde 2 (el primer posible divisor, ya que 1 siempre es divisor)
    # hasta la raiz cuadrada del numero ingresado.
    # ¿Por que hasta la raiz cuadrada?
    # Si un numero 'num' tiene un divisor mayor que su raiz cuadrada,
    # tambien tendra un divisor mas pequeño que su raiz cuadrada.
    # Por ejemplo, para 100, la raiz es 10. Si 20 es divisor (20 > 10), entonces 5 (100/20) tambien lo es (5 < 10).
    # 'int(num**0.5)' calcula la raiz cuadrada y la convierte a entero (truncando decimales).
    # '+ 1' es necesario porque 'range()' excluye el limite superior.
    for i in range(2, int(num**0.5) + 1):
        # 5. Comprobar si 'i' es un divisor:
        # El operador '%' (modulo) da el resto de una division.
        # Si 'num % i == 0', significa que 'i' divide a 'num' exactamente,
        # lo que indica que 'num' tiene un divisor aparte de 1 y el mismo 'num'.
        if num % i == 0:
            # Si encontramos un divisor, el numero NO es primo.
            es_primo = False
            # 'break' es una palabra clave que detiene el bucle 'for' inmediatamente.
            # No tiene sentido seguir buscando mas divisores si ya encontramos uno.
            break

# 6. Mostrar el resultado final:
# Despues de que el bucle termina (o si se manejó un caso especial al principio),
# verificamos el valor final de nuestra bandera 'es_primo' para imprimir el mensaje adecuado.
if es_primo:
    print(f"{num} es un numero primo.")
else:
    print(f"{num} no es un numero primo.")