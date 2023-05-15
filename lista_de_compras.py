import os

lista = []

while True:
    comand = input('Digite um comando\n[i]nserir - [a]pagar - [l]istar:')
    if comand == 'l':
        os.system('cls')
        if not lista:
            print('Lista Vazia')
            continue #desnecessário, porém eu quis
        for i, item in enumerate(lista):#não faria nada em lista vazia
            print(i, item)
    
    elif comand == 'i':
        os.system('cls')
        lista.append(input('Digite o item a ser inserido:\n'))
    
    elif comand == 'a':
        try:
            apagar_item = int(input('Digite o indice a ser apagado:'))
            del lista[apagar_item]
            os.system('cls')
        except IndexError:
            os.system('cls')
            print('Esse indice não existe')
        except ValueError:
            os.system('cls')
            print('Digite um número int. para índice')        
    else:
        os.system('cls')
        print('Digite um comando válido')

print('saí do while')