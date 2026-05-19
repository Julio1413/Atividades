maior=0
menor=None
for i in range(10):
    numero = int(input(f'({i+1}/50)Digite um número inteiro: '))
    if maior < numero: maior = numero
    if not menor: menor = numero
    elif menor > numero: menor = numero
    
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
            