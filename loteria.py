import random

print("Hola y ¡BIENVENIDO! a tu simulador de lotería")

# Menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Jugar lotería")
    print("2. Ver historial de intentos")
    print("3. Salir")

def jugar_loteria(intentos):
    print("Comenzamos a jugar")
    
    # Solicitar al usuario que ingrese un número de 6 dígitos
    while True:
        user_number = input("Ingrese un número de 6 dígitos: ")
        if user_number.isdigit() and len(user_number) == 6:
            user_number = int(user_number)
            break
        else:
            print("Por favor, ingrese un número válido de 6 dígitos.")
    
    # Generar un número aleatorio de 6 dígitos
    random_number = generate_random_number()
    
    # Comparar los números y contar los dígitos correctos
    correct_digits = compare_numbers(user_number, random_number)
    
    # Almacenar el intento en el historial
    intentos.append((user_number, random_number, correct_digits))
    
    # Mostrar el resultado
    print(f"Número ingresado: {user_number}")
    print(f"Número de loteria: {random_number}")
    print(f"Número de dígitos correctos: {correct_digits}")

def ver_historial_de_intentos(intentos):
    if not intentos:
        print("No has realizado ningún intento.")
    else:
        print("Tus intentos son:")
        for i, intento in enumerate(intentos, 1):
            print(f"Intento {i}: Tu número: {intento[0]}, Número de loteria: {intento[1]}, Dígitos correctos: {intento[2]}")

def salir():
    print("Adiós, ¡nos vemos pronto!")

def generate_random_number():
    return random.randint(100000, 999999)

def compare_numbers(user_number, random_number):
    user_number_str = str(user_number)
    random_number_str = str(random_number)
    
    correct_digits = 0
    for i in range(len(user_number_str)):
        if user_number_str[i] == random_number_str[i]:
            correct_digits += 1
    
    return correct_digits

# Lista para almacenar los intentos
historial_intentos = []

# Bucle principal
while True:
    mostrar_menu()
    opcion_seleccionada = int(input("Selecciona una opción (1-3): "))

    if opcion_seleccionada == 1:
        jugar_loteria(historial_intentos)
    elif opcion_seleccionada == 2:
        ver_historial_de_intentos(historial_intentos)
    elif opcion_seleccionada == 3:
        salir()
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")
