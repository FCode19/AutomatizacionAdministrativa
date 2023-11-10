import random

def generar_numeros():
    return [random.randint(1, 50) for _ in range(6)]

def jugar_tinka():
    print("¡Bienvenido a la TINKA!")

    numeros_tinka = generar_numeros()
    intentos_restantes = 6
    print(numeros_tinka)
    while intentos_restantes > 0:
        try:
            numeros_usuario = [int(x) for x in input("Ingresa 6 números de la TINKA (separados por espacio): ").split()]
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if set(numeros_usuario) == set(numeros_tinka):
            print("¡Ganaste la TINKA, tu premio son 5 millones!")
            print("Los números de la suerte fueron:", numeros_tinka)
            break
        else:
            print("Intento incorrecto. Te quedan {} intentos.".format(intentos_restantes - 1))

        intentos_restantes -= 1

    else:
        print("Lo siento, has agotado tus intentos. Los números de la suerte fueron:", numeros_tinka)

if __name__ == "__main__":
    jugar_tinka()
