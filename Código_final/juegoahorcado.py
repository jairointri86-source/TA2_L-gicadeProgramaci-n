import random

def jugar_ahorcado():
    # Lista de palabras
    palabras = ["cobra", "camaleon", "cocodrilo", "avestruz", "delfin", "elefante", "jirafa", "leon", "mono", "tigre"]
    palabra = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos = 5
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0:
        # Mostrar la palabra oculta
        palabra_oculta = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += "_"
        
        print(f"\nPalabra: {palabra_oculta}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(letras_adivinadas)}")
        
        # Verificar si ganó
        if "_" not in palabra_oculta:
            print("¡Felicidades has ganado! Eres un pro para adivinar palabras.")
            break
        
        # Pedir letra
        intento = input("Adivina una letra: ").lower()
        
        # Validar entrada
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue
        
        if intento in letras_adivinadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue
            
        letras_adivinadas.append(intento)
        
        # Comprobar si la letra está en la palabra
        if intento in palabra:
            print(f"¡Bien! La letra '{intento}' está en la palabra.")
        else:
            intentos -= 1
            print(f"Lo siento, la letra '{intento}' no está en la palabra.")
            
    if intentos == 0:
        print(f"\n¡Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()
