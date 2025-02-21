print("Hola y ¡BIENBENIDO! a tu simulador de loteria")

#Menú
def mostrar_menu():
    print("Menú:")
    print("1. Jugar loteria 1")
    print("2. Ver historial de intentos 2")
    print("3. Salir 3")

def jugarLoteria_1():
    print("Comenzemos a jugar")
    

def verHistorialDeIntentos_2():
    print("Tus intentos son")

def salir_3():
    print("Adiós nos vemos pronto")

# Variable para almacenar la opción seleccionada
opcion_seleccionada = 0

# Mostrar el menú y solicitar una opción al usuario
while opcion_seleccionada not in [1, 2, 3]:
    mostrar_menu()
    opcion_seleccionada = int(input("Selecciona una opción (1-3): "))

# Ejecutar la opción seleccionada
if opcion_seleccionada == 1:
    jugarLoteria_1()
elif opcion_seleccionada == 2:
    verHistorialDeIntentos_2()
elif opcion_seleccionada == 3:
    salir_3()

import random

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

# Solicitar al usuario que ingrese un número de 6 dígitos
user_number = int(input("Ingrese un número de 6 dígitos: "))

# Generar un número aleatorio de 6 dígitos
random_number = generate_random_number()

# Comparar los números y contar los dígitos correctos
correct_digits = compare_numbers(user_number, random_number)

# Mostrar el resultado
print(f"Número ingresado: {user_number}")
print(f"Número aleatorio: {random_number}")
print(f"Número de dígitos correctos: {correct_digits}")




