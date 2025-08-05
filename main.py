# Crea un bucle que recorra los números del 1 al 1000
for numero in range(1, 1001):
    # Condición para "Fizzbuzz: Número divisible entre 3 y 5. Si un número es divisible por 3 y 5, lo es por 15; así evitamos un error lógico común "
    if numero % 15 == 0:
        print("Fizzbuzz")
    # Condición para "Fizz: Número divisible entre 3"
    elif numero % 3 == 0:
        print("Fizz")
    # Condición para "Buzz: Número divisible entre 5"
    elif numero % 5 == 0:
        print("Buzz")
    # Condición por defecto (imprimir el número): Si no cumple ninguna de las condiciones antes mencionadas.
    else:
        print(numero)