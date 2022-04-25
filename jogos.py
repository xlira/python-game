import forca
import adivinhacao

print("*********************************")
print("***Bem vindo ao jogo de Forca!***")
print("*********************************")

def jogar():

    print("Escolha um jogo para jogo:")
    jogo = int(input("(1) Adivinhação (2) Forca: "))

    if(jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()
    else:
        print("Você precisa digitar um numero entre 1 e 2, (1) Adivinhação (2) Forca ")

if(__name__ == "__main__"):
    jogar()
