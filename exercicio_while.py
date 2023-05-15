nome = input('Digite um nome: ')
cont = 0
novo = ''

while cont<len(nome):
    letra = nome[cont]
    novo += f'*{letra}'
    cont +=1
novo+='*'

print(novo)