nome = input('Qual o seu primeiro nome? ')
nome_tamanho = len(nome)

if nome.isdigit() == True:
    print('Escreva um nome válido')
else:
    if nome_tamanho > 1:
        if nome_tamanho <= 4:
            print('Seu nome é pequeno')
        elif nome_tamanho == 5 or nome_tamanho == 6:
            print('Seu nome tem um tamanho normal.')
        elif nome_tamanho > 6:
            print('Seu nome é grande!')
    else:
        print('Digite mais de uma letra')