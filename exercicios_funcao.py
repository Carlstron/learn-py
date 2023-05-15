import sys
import os
def multiplicador(mult):
    def vezes(numero):
        return numero * mult
    return vezes

duplicate = multiplicador(2)
triplicate = multiplicador(3)
quadruplicate = multiplicador(4)
try:
   n = int(input('digite um número: '))
except ValueError:
    print('você digitou um valor inválido')


print(f'{n} duplicado é:', duplicate(n))
print(f'{n} triplicado é:', triplicate(n))
print(f'{n} quadruplicado é:', quadruplicate(n))
