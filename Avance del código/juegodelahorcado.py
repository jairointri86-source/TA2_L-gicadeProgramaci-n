import random

def jugar_ahorcado():
    # Lista de palabras
    palabras = ['casa', 'zapato', 'bandera', 'computadora', 'desarrollo']
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos = 6
    
    print("¡Bienvenido al Juego el Ahorcado!")

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

