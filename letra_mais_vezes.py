frase = input('Digite uma frase: ')

i=0
qtd=0
letra=''
while i< len(frase):
    if frase[i] == ' ':
        i += 1
        continue
    if frase.count(frase[i])>qtd:
        qtd = frase.count(frase[i])
        letra = frase[i]
    i+=1

print('a letra que repetiu mais vezes foi:', 
      letra, '\nRepetiu', qtd, 'X')