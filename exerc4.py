horario_text = (input('Que horas são? '))
try:
    horario = int(horario_text)
    if horario >= 0 and horario <= 11:
        if horario == 1:
            print(f'É {horario} hora, Bom dia!')
        else:
            print(f'São {horario} horas, Bom dia!')
    elif horario >= 12 and horario <= 17:
        print(f'São {horario} horas, Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print(f'São {horario} horas, Boa noite!')
except:
    print('Digite um valor válido! ')