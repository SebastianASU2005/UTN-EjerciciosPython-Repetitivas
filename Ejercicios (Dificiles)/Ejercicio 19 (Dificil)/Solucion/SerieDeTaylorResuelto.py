# Este programa calcula una aproximacion del valor de e^x (e elevado a la potencia de x)
# usando la serie de Taylor. La serie de Taylor es una forma de representar funciones
# como una suma infinita de terminos.

# La formula de la serie de Taylor para e^x es:
# e^x = 1 + x/1! + x^2/2! + x^3/3! + ... + x^n/n!
# Donde:
# - 'x' es el numero que queremos elevar con 'e'.
# - 'n!' (n factorial) es el producto de todos los enteros positivos hasta n (ej. 3! = 3*2*1 = 6).
# - Los puntos suspensivos indican que la serie continua infinitamente, pero nosotros
#   la aproximaremos usando un numero limitado de terminos.

# 1. Solicitar los valores de 'x' y el numero de terminos:
# 'input(...)' pide al usuario el valor de 'x'. 'float(...)' lo convierte a un numero decimal,
# ya que 'x' puede ser un numero con decimales.
x = float(input("Ingresa el valor de x: "))
# Pedimos el numero de terminos que usaremos en la suma para la aproximacion.
# 'int(...)' lo convierte a un numero entero. Cuantos mas terminos, mas precisa sera la aproximacion.
n_terminos = int(input("Ingresa el numero de terminos para la aproximacion: "))

# 2. Inicializar variables:
# 'e_a_la_x = 0' es la variable donde acumularemos la suma de los terminos de la serie.
# La inicializamos en 0 antes de empezar a sumar.
e_a_la_x = 0

# 'termino_actual = 1' representa el valor del termino actual que estamos calculando.
# Lo inicializamos en 1 porque el primer termino de la serie (cuando i=0) es x^0 / 0!, que es 1/1 = 1.
termino_actual = 1

# 'factorial = 1' es la variable que guardara el factorial de 'i' en cada paso.
# Tambien se inicializa en 1 porque 0! (factorial de 0) es 1, que es el denominador
# del primer termino.
factorial = 1

# 3. Bucle 'for' para calcular y sumar los terminos:
# Este bucle se ejecutara 'n_terminos' veces, una vez por cada termino que queremos sumar.
# 'i' representara el indice del termino actual (0, 1, 2, ... n_terminos-1).
for i in range(n_terminos):
    # 4. Calcular el factorial y la potencia (para terminos despues del primero):
    # El primer termino (i=0) es un caso especial (x^0 / 0! = 1).
    # Para todos los demas terminos (cuando 'i' es mayor que 0), necesitamos calcular
    # el nuevo factorial y el nuevo valor de x elevado a la potencia 'i'.
    if i > 0:
        # 'factorial *= i' es lo mismo que 'factorial = factorial * i'.
        # Calcula el factorial de 'i' de forma acumulativa.
        # Ejemplo: si i=1, factorial=1*1=1. Si i=2, factorial=1*2=2. Si i=3, factorial=2*3=6, etc.
        factorial *= i
        
        # 'termino_actual = (x**i) / factorial' calcula el valor del termino actual:
        # - 'x**i' eleva 'x' a la potencia 'i'.
        # - Lo divide por el 'factorial' que acabamos de calcular.
        termino_actual = (x**i) / factorial
    
    # 5. Sumar el termino actual a la aproximacion total:
    # 'e_a_la_x += termino_actual' suma el valor del termino que acabamos de calcular
    # a nuestra variable acumuladora 'e_a_la_x'.
    e_a_la_x += termino_actual
    
# 6. Mostrar el resultado:
# Una vez que el bucle ha sumado todos los 'n_terminos' especificados,
# se imprime la aproximacion final de e^x.
print(f"Aproximacion de e^{x} con {n_terminos} terminos: {e_a_la_x}")