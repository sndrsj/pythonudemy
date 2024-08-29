   
num = (input('Digite um número inteiro: '))
if num.isdigit():
            numInt = int(num)
            if numInt % 2 == 0:
                    print(f'O número {numInt} é par')
            else:
                    print(f'O número {numInt} é impar')
else:
    print('Voce nao digitou um numero inteiro')

