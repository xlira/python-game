import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 2
rodada = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Facíl  (2) Médio  (3) Difícil")

nivel = int(input("Defina o nível:"))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas =5

while (total_de_tentativas > 0 ):
    print("Rodada:", rodada)
    print("Total de tentavidas: {}".format( total_de_tentativas))
    chute_bruto = input("Digite um numero: ")
    print ("Vocêr digitou:", chute_bruto)
    chute = int(chute_bruto)

    if(chute < 1 or chute >100):
        print("Você precisa indicar um numero entre 1 e 100")
        continue

    if (chute == numero_secreto):
        print("Você acertou! Sua pontuação foi {} pontos!".format(pontos))
        break

    if (total_de_tentativas < 1):
        print("As tentativas acabaram!")
        break

    else:
        if(chute > numero_secreto):
            print("Você errou! O numero secreto é menor que o numero inserido!")
        if(chute < numero_secreto):
            print("Você errou! O numero secreto é maior que o numero inserido"!)
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada + 1
print("Fim do jogo!")
