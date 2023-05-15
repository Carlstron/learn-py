import os

soma1 = 0
soma2 = 0
cpf = '996.913.350-00'

if len(cpf)<14:
    print('CPF menor do que deveria, digite com "." e "-"')
cpfl = list(cpf)
cpfl.remove('.')
cpfl.remove('.')
cpfl.remove('-')

print(*cpfl)
exit()
digitos = cpfl.pop(-2),cpfl.pop(-1)
for i, d in enumerate(cpfl):
    cpfl[i] = int(d)
    mult = 10-i
    soma1 += cpfl[i]*mult
digito1 = (soma1*10)%11 if (soma1*10)%11 < 10 else 0
if str(digito1) != digitos[0]:
    print('CPF inválido')

cpfl.append(digito1)
for i, d in enumerate(cpfl):
    mult = 11-i
    soma2 += cpfl[i]*mult
digito2 = (soma2*10)%11 if (soma2*10)%11 < 10 else 0
if str(digito2) != digitos[1]:
    print('CPF inválido')

print(cpfl, digitos,soma1,digito1,soma2,digito2, sep='\n')