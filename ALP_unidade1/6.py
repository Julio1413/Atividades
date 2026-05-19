bosonaro=0 #1
lula=0 #2
eneas=0 #3
ciro=0 #4
nulo = 0 #5
branco = 0 #6

voto=-1
while True:
    print('Candidatos:')
    print('1 - Bosonaro')
    print('2 - Lula')
    print('3 - Eneas')
    print('4 - Ciro')
    print('5 - Nulo')
    print('6 - Branco')
    voto = int(input(f'Digite o número do seu candidato (0 para sair): '))
    if voto == 1:bosonaro += 1
    elif voto == 2:lula += 1
    elif voto == 3:eneas += 1
    elif voto == 4:ciro += 1
    elif voto == 5:nulo += 1
    elif voto == 6:branco += 1
    elif voto == 0:break
    
print(f'Bosonaro: {bosonaro} votos')
print(f'Lula: {lula} votos')
print(f'Eneas: {eneas} votos')
print(f'Ciro: {ciro} votos')
print(f'Nulo: {nulo} votos')
print(f'Branco: {branco} votos')
