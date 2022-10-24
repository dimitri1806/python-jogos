print('******************************')
print('Qual meu numero da sorte?')
print('******************************')

numero_secreto  = 18
total_de_tentativas = 5


while(total_de_tentativas > 0):
    print('Chances:', total_de_tentativas)
    chute_str = input('Faça seu primeiro chute:')

    print('Você chutou', chute_str)
    chute = int(chute_str)

    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    acertou = numero_secreto == chute

    if (acertou):
        print('Você acertou!')
    else:
        if(maior):
            print('Você errou! O seu chute foi maior que o meu número da sorte!')
        elif(menor):
            print('Você errou! O seu chute foi menor que o meu número da sorte!')
    total_de_tentativas = total_de_tentativas - 1

print('Fim do jogo')