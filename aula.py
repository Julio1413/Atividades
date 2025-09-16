lista = []
lista_c=''
while lista_c !='Fim':
    print(lista)
    lista_c = input('Adicione ou remova itens da lista acima ou digite "Fim" para sair:')
    ls3 = input("digite o que deseja adicionar ou remover:")
    if lista_c == 'remover': lista.remove(ls3)
    elif lista_c == 'adicionar': lista.append(ls3)
    else: print('Comando inválido, tente novamente!')