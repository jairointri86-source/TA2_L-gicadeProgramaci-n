import random

def jugar_ahorcado():
    # Lista de palabras
    palabras = ['python', 'programacion', 'ahorcado', 'computadora', 'desarrollo']
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos = 6
    
    print("¡Bienvenido al Ahorcado!")

    while intentos > 0:
        # Mostrar el estado actual de la palabra
        estado_palabra = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_palabra += letra
            else:
                estado_palabra += "_"
        print(f"\nPalabra: {estado_palabra}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(letras_adivinadas)}")

        # Comprobar si ganó
        if "_" not in estado_palabra:
            print("¡Felicidades! ¡Has ganado!")
            break

        # Pedir letra
        intento = input("Adivina una letra: ").lower()

        # Validación
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, introduce una sola letra válida.")
            continue
        if intento in letras_adivinadas:
            print("Ya has probado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(intento)

        # Comprobar si la letra está en la palabra
        if intento not in palabra_secreta:
            intentos -= 1
            print("Letra incorrecta.")
        else:
            print("¡Bien hecho!")

        if intentos == 0:
            print(f"\n¡Perdiste! La palabra era: {palabra_secreta}")

# Iniciar el juego
if __name__ == "__main__":
    jugar_ahorcado()
