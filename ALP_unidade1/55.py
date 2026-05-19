
diasmes = 30
meses = 12
diasano  = 365
data1 = input('Digite a primeira data (ddmmaaaa): ')
data2 = input('Digite a segunda data (ddmmaaaa): ')


if data1[4:] == data2[4:]:
    if int(data1[2:4]) == int(data2[2:4]):
        if int(data1[:2]) == int(data2[:2]):
            print('As datas são iguais.')
        else:
            print(f'A diferença entre as datas é de {abs(int(data1[:2]) - int(data2[:2]))} dias.')
    else:
        print(f'A diferença entre as datas é de {abs(int(data1[:2]) - int(data2[:2])+diasmes*(int(data2[2:4]) - int(data1[2:4])))} dias.')
else:
    print(f'A diferença entre as datas é de {abs(int(data1[:2]) - int(data2[:2])+diasmes*(int(data2[2:4]) - int(data1[2:4]))+diasano*(int(data2[4:]) - int(data1[4:])))} dias.')