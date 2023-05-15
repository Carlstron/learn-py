import sys
fatores = ''
d = 1
def mult(*args):
    # lista = list(args)
    resultado = 1
    if args == ():
        return 0
    for d in args:
        try:
            resultado *= int(d)
        except ValueError:
            print('Tem caracteres inválidos')
            return None  
        if resultado == 0:
            print('há um 0 na conta')
            return 0
    return resultado

while d != '=':
    d = input('Digite um número para multiplicar\n ou digite "=" para ver o resultado: ')
    try:
        if d == '=':
            continue
        int(d)
        fatores += d
        
    except ValueError:
        print('você digitou um valor inválido')

m = mult(*fatores)
print(1*2*3*4*5)
print(m)

