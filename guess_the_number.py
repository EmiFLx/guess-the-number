import random
print("¡Bienvenido al juego de adivinar el número!")
print("A) Nivel facil: Adivina un número entre 1 y 10.")
print("B) Nivel medio: Adivina un número entre 1 y 50.")
print("C) Nivel difícil: Adivina un número entre 1 y 100.")
dificultad = input ("Selecciona el nivel de dificultad (A, B o C): ").upper()
if dificultad == "A":
    maximo = 10
elif dificultad == "B":  
    maximo = 50
elif dificultad == "C":
    maximo = 100
else:
    print("Opción no válida. Se seleccionará el nivel fácil por defecto.")
    maximo = 10

numero = random.randint(1, maximo)
intentos = 0

print()
while True:
    intentos += 1
    num_user = int(input("Ingresa tu número: "))
    if num_user < 1 or num_user > maximo:
        print(f"Número fuera de rango. Por favor, ingresa un número entre 1 y {maximo}.")
    elif num_user < numero:
        print("El número es mayor. Intenta de nuevo.")
    elif num_user > numero:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero} en {intentos} intentos.")
        break
    