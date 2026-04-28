pessoas =[]
import os


def adicionar_habitante():
    nome = input('Digite o nome do habitante: ')
    salario = int(input('Digite o valor de seu salário: '))
    filhos = int(input('Digite seu número de filhos: '))
    pessoas.append({'nome':nome,'salario':salario,'filhos':filhos})
    os.system('clear')
    print('Habitante adicionado com sucesso!')

def sair_e_resultados():
    total_salario = 0
    maior_salario = 0
    salario_100 = 0
    total_filhos = 0
    for habitante in pessoas:
        total_salario += habitante['salario']
        total_filhos += habitante['filhos']

        if habitante['salario'] <= 100:
            salario_100 +=1
        if habitante['salario'] >maior_salario:
            maior_salario = habitante['salario']

    os.system('clear')
    print('-----Resultados-----')
    print(f'Média do salário: {(total_salario/len(pessoas))}')
    print(f'Média de filhos: {(total_filhos/len(pessoas))}')
    print(f'Maior salário: {maior_salario}')
    print(f'Salário até R$100,00: {salario_100}')


while True:
    print('Digite sua ação:')
    print('1 - Adicionar Habitante:')
    print('2 - Sair e exibir resultados:')
    comando = int(input('Ação: '))

    if comando ==1:
        adicionar_habitante()
    elif comando ==2:
        sair_e_resultados()
        break