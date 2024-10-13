palavraSecreta = 'macaco'
resultadoPalavra = '*'*len(palavraSecreta)
tentativa = 0
letrasAcertadas = ''

while True:
    userResponse = input('Digite sua tentativa: ')

    if userResponse in letrasAcertadas:
        print('Você já digitou essa letra.')
        continue

    if len(userResponse) > 1:
        print('Digite apenas uma letra.')
        continue

    if userResponse in palavraSecreta:
        letrasAcertadas += userResponse

    palavraFormada = ''
    for letra in palavraSecreta:
        if letra in letrasAcertadas:
                palavraFormada += letra
        else:
                palavraFormada += '*'
    
    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        print('Você venceu!')
        break