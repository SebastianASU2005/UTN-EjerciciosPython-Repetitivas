# Este programa cuenta la cantidad de cifras (digitos) que tiene un numero entero
# que el usuario ingresa. Por ejemplo, si ingresas 123, dira que tiene 3 cifras;
# si ingresas -5432, dira que tiene 4 cifras.

# 1. Solicitar el numero al usuario:
# 'input(...)' muestra el mensaje y espera que el usuario escriba un numero entero.
# 'int(...)' convierte el texto ingresado a un numero entero.
num = int(input("Ingresa un numero entero para contar sus cifras: "))

# 2. Manejar el caso especial del numero cero:
# El numero 0 es el unico caso donde nuestro bucle no funcionaria directamente (ya que 0 no es > 0).
# Por definicion, el numero 0 tiene 1 cifra.
if num == 0:
    print("El numero 0 tiene 1 cifra.")
else:
    # 3. Preparar el numero para el conteo:
    # 'num_abs = abs(num)' obtiene el valor absoluto del numero.
    # Esto es importante para que el programa funcione correctamente con numeros negativos.
    # Por ejemplo, las cifras de -123 son las mismas que las de 123.
    num_abs = abs(num)
    
    # 'contador_cifras = 0' es una variable que usaremos para llevar la cuenta de las cifras.
    # La inicializamos en 0 porque aun no hemos contado ninguna.
    contador_cifras = 0
    
    # 'temp_num = num_abs' creamos una copia del numero absoluto para trabajar con ella
    # dentro del bucle sin modificar el valor original que necesitamos para el mensaje final.
    temp_num = num_abs
    
    # 4. Bucle 'while' para contar las cifras:
    # Este bucle se ejecuta MIENTRAS 'temp_num' sea mayor que 0.
    # En cada repeticion, eliminamos un digito del final del numero y aumentamos el contador.
    while temp_num > 0:
        # 'temp_num //= 10' es una division entera. Divide 'temp_num' por 10 y asigna
        # el resultado (sin la parte decimal) de vuelta a 'temp_num'.
        # Esto efectivamente "elimina" el ultimo digito del numero en cada paso.
        # Ejemplo:
        #   Si temp_num es 123: 123 // 10 = 12. contador_cifras = 1.
        #   Si temp_num es 12:  12 // 10 = 1.  contador_cifras = 2.
        #   Si temp_num es 1:   1 // 10 = 0.  contador_cifras = 3.
        temp_num //= 10
        
        # 'contador_cifras += 1' incrementa nuestro contador en 1 cada vez que eliminamos un digito.
        # Esto significa que hemos contado una cifra mas.
        contador_cifras += 1
    
    # 5. Mostrar el resultado final:
    # Cuando el bucle termina (porque 'temp_num' llego a 0, lo que significa que
    # ya no quedan digitos), se imprime la cantidad de cifras encontradas.
    print(f"El numero {num} tiene {contador_cifras} cifras.")