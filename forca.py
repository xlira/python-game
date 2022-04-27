
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    print("Jogo da Forca.")

    palavra = 'banana'
    acertou = False
    forcou = False

    while ( not acertou and not forcou):
        for letra in palavra:
            print(letra)


if(__name__ == "__main__"):
    jogar()
