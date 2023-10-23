from celsius_fahrenheit import fah, cel
while True:


    print('\n\t\t\t --- Conversor de Temperatura entre C° e F° --- \n')
    #menu
    print('1. Fahrenheit')
    print('2. Celsius')
    print('3. Saida')

    op = int(input('\n\tOpção: '))

    if op == 1:
        print('\nFahrenheit\n')

        #entrada
        v1 = int(input('digite um numero: '))

        #processamento
        total = fah(v1)

        #saida
        print(f'\n{v1} C° = {total}F°\n')
    elif op == 2:
        print('\nCelsius\n')

        #entrada
        v1 = int(input('digite um numero: '))

        #processamento
        total = cel(v1)

        #saida
        print(f'\n{v1} F° = {total}C°\n')

    elif op == 3:
        print('Até logo')
        break
    else:
        print('Erro opção nao existe')
