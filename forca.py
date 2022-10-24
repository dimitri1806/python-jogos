
print('***************************')
print('Bem vindo ao jogo da Forca!')
print('***************************')

palavra_secreta = 'banana'.upper()
letras_acertadas = ['-' for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

while(not enforcou and not acertou):

    chute = input('Qual letra?')
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if( chute == letra ):
                letras_acertadas[index] = letra
            index = index +1
    else:
        erros = erros + 1
    enforcou = erros == 6
    acertou = '-' not in letras_acertadas

    print(letras_acertadas)

print('Fim do jogo')