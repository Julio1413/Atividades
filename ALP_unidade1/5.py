numero = 0
numero_media = 0
contador = 0
while numero>=0:
    numero = int(input('Digite um número inteiro (negativo para sair): '))
    if numero >= 0:
        numero_media += numero
        contador += 1
print(f'A média dos números digitados é: {numero_media/contador}')
