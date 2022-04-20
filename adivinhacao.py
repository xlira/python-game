print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_bruto = input("Digite um numero: ")

chute = int(chute_bruto)

print("Você digitou: ", chute)

if (chute == numero_secreto):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! O numero secreto é menor que o numero inserido")
    if(chute < numero_secreto):
        print("Você errou! O numero secreto é maior que o numero inserido")
print("Fim do jogo!")
