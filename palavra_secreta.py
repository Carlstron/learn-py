import os
ps = 'dois'
la = ''
pformada = ''
t=0
while pformada != ps:
    ld = input('Digite uma letra:')
    t +=1

    if len(ld)>1:
        print('Digite apenas uma letra')
        continue
    if ld in ps:
        la += ld

    pformada = ''
    for ls in ps:
        if ls in la:
            pformada += ls
        else: pformada += '*'
    print(pformada)
os.system('cls')
print(f'Parabéns, você acertou\nA palavra era {ps}\n Você tentou {t} vezes')

