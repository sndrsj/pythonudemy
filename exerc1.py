nome = 'Sandro'
sobrenome = 'Souza'
idade = 20
ano_nascimento = 2003
altura_metros = 1.71
def maioridade():
    if 2024 - ano_nascimento >= 18:
        maior_idade = True
    else:
        maior_idade = False
    if maior_idade == True:
        return 'Sim'
    else:
        return 'Não'
    
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de Nascimento: ', ano_nascimento)
print('É maior de idade? ', maioridade())
print('Altura em metros: ', altura_metros)