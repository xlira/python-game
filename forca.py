
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    print("Jogo da Forca.")

    palavra = 'banana'
    acertou = False
    forcou = False

    while ( not acertou and not forcou):

        chute = input("Qual a letra?")

        index = 0
        for letra in palavra:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}.".format(letra, index))
            index = index + 1



if(__name__ == "__main__"):
    jogar()
