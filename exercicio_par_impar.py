num_str = input('Digite um número Inteiro: ')

if '.' in num_str:
    print(f'{num_str} não é um número inteiro')
elif int(num_str) % 2 == 0:
    print(f'{num_str} é um numero par')
else: print(f'{num_str} é um numero impar')

# hora_str = input('Digite o horário (apenas horas inteiras): ')
# hora = int(hora_str)
# if hora <= 24 and hora >= 0:
#     if hora <= 11 and hora >= 3:
#         print('Bom Dia')
    
#     elif hora >= 12 and hora <= 17:
#         print('Boa Tarde')
    
#     else:
#         print('Boa Noite')
# else: print('Hora inválida')

# nome = input('Digite o seu Nome: ')
# if len(nome) <= 5:
#     print('Seu nome é Curto')
# elif len(nome) == 5:
#     print('Seu nome é Normal')
# else : print('Seu nome é Longo')