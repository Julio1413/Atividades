numero= int(input('Digite um número: '))

if numero%2 == 0:
    divisores = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            divisores +=1
    print(f'O número {numero} é par e tem {divisores} divisores.')
elif numero%2 !=0 and numero <10:
    import math
    fatorial = math.factorial(numero)
    print(f'O número {numero} é ímpar e menor que 10, seu fatorial é {fatorial}.')
else:
    for i in range(1, numero+1):
        print(i)