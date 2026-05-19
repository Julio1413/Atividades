cod = 1


while cod != '0':
    print('Digite o comando:')
    print('1 - Adicionar aluno')
    print('0 - Encerrar programa')
    
    cod = (input('Comando: '))
    if cod == '1':
        nome = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        media = (nota1 + nota2 + nota3) / 3
        print(f'A média de {nome} é {media:.2f}')
    elif cod == '0':
        print('Encerrando programa...')
    else:
        print('Comando inválido. Tente novamente.')