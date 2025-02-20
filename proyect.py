print("Hola y ¡BIENBENIDO! a tu simulador de loteria")

#Menú
def mostrar_menu():
    print("1. jugar loteria")
    print("2. salir")

def jugarLoteria():
    print("comensemos a jugar")

def salir():
    print("Adios asta luego")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            jugarLoteria()
        elif opcion == '2':
            salir()
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

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




