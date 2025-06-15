# Este programa toma un numero entero ingresado por el usuario y lo "invierte",
# es decir, muestra sus digitos en orden inverso. Por ejemplo, si ingresas 123,
# el programa mostrara 321. Si ingresas -456, mostrara -654.

# 1. Solicitar el numero al usuario:
# 'input(...)' pide al usuario que ingrese un numero entero.
# 'int(...)' convierte esa entrada de texto a un numero entero.
numero_original = int(input("Ingresa un numero entero para invertirlo: "))

# 2. Inicializar variables:
# 'numero_invertido = 0' es donde construiremos el numero con los digitos invertidos.
# Lo inicializamos en 0 porque aun no hemos procesado ningun digito.
numero_invertido = 0

# 'temp_numero = abs(numero_original)' crea una copia del numero original.
# Usamos 'abs()' (valor absoluto) para trabajar solo con la parte positiva del numero.
# Esto simplifica el proceso de extraer los digitos, sin preocuparnos por el signo
# hasta el final. Si el numero original era negativo, lo manejaremos al final.
temp_numero = abs(numero_original)

# 3. Bucle 'while' para extraer y construir el numero invertido:
# Este bucle continuara ejecutandose mientras 'temp_numero' sea mayor que 0.
# Cada iteracion extraera el ultimo digito de 'temp_numero' y lo agregara a 'numero_invertido'.
while temp_numero > 0:
    # a. Extraer el ultimo digito:
    # 'digito = temp_numero % 10' usa el operador modulo (%).
    # Esto nos da el resto de la division de 'temp_numero' por 10,
    # que es siempre el ultimo digito del numero.
    # Ejemplo: 123 % 10 es 3.
    digito = temp_numero % 10
    
    # b. Construir el numero invertido:
    # 'numero_invertido = numero_invertido * 10 + digito'
    # Esta linea es crucial. Hace dos cosas:
    #   - 'numero_invertido * 10': Desplaza los digitos que ya hemos procesado
    #     una posicion a la izquierda (ej. si era 3, ahora es 30).
    #   - '+ digito': Agrega el nuevo digito extraido a la derecha.
    # Ejemplo con 123:
    #   - 1ra iteracion (digito=3): numero_invertido = 0 * 10 + 3 = 3
    #   - 2da iteracion (digito=2): numero_invertido = 3 * 10 + 2 = 32
    #   - 3ra iteracion (digito=1): numero_invertido = 32 * 10 + 1 = 321
    numero_invertido = numero_invertido * 10 + digito
    
    # c. Eliminar el ultimo digito de 'temp_numero':
    # 'temp_numero //= 10' usa la division entera (//).
    # Esto elimina el ultimo digito de 'temp_numero'.
    # Ejemplo: 123 // 10 es 12. Luego 12 // 10 es 1. Luego 1 // 10 es 0.
    temp_numero //= 10

# 4. Manejar el signo original:
# Despues de que el bucle termina, 'numero_invertido' contiene la version positiva invertida.
# Si el 'numero_original' era negativo, necesitamos aplicar el signo negativo al resultado.
if numero_original < 0:
    numero_invertido *= -1 # Multiplicar por -1 para hacer el numero negativo

# 5. Mostrar el resultado final:
# Se imprime el numero invertido, incluyendo su signo si es que lo tenia.
print(f"El numero invertido es: {numero_invertido}")