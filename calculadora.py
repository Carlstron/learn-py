while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        op = input('Digite o operador desejado: ')

        if op == '+':
            print(f'{n1} {op} {n2} =', n1+n2)
        elif op == '-':
            print(f'{n1} {op} {n2} =', n1-n2)
        elif op == '*':
            print(f'{n1} {op} {n2} =', n1*n2)
        elif op == '/':
            print(f'{n1} {op} {n2} =', f'{(n1/n2):.03f}')
        else:
            print(f'Desculpe, o operador {op} não é compatível')


        print(n1, op, n2)


        sair = input('Você quer sair? [s]im: ').lower().startswith('s')
        if sair:
            break
    except:
        print('vc não digitou um caracter válido')
        sair = input('Você quer sair? [s]im: ').lower().startswith('s')
        if sair:
            break