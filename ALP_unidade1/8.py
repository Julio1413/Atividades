total_pares =0
contador = 0
numero = 1
while numero != 0:
    numero = int(input('Digite um número inteiro (negativo para sair): '))
    if numero % 2 == 0:
        contador += 1
        total_pares += numero
contador-=1
print(f'Foram digitados {contador} números pares, com a media total de {total_pares/contador}.')