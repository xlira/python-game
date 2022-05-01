import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    print("Jogo da Forca.")

    arquivo = open("palavras.txt", "r")
    palavras= []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()

    print(palavra)
    letras_acertadas = ["_" for letra in palavra]

    acertou = False
    forcou = False
    erros = 0

    print(letras_acertadas)

    while ( not acertou and not forcou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra):
            index = 0
            for letra in palavra:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posição {}.".format(letra, index))
                index = index + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


if(__name__ == "__main__"):
    jogar()
