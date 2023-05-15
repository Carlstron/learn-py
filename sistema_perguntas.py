import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
for p in perguntas:
    print(p['Pergunta'])
    for i, o in enumerate(p['Opções']):
        print(f'{i}-) {o}')
    try:
        r = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Você errou')
        continue
    if p['Opções'][r] == p['Resposta']:
        print('Você acertou!\n')
        acertos += 1
    else: print('Você errou')

print(f'\n\n Você acertou {acertos} de {len(perguntas)} perguntas!!')