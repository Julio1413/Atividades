
while True:
    nota1 = float(input('Digite a primeira nota do aluno (ou -1 para encerrar): '))
    nota2 = float(input('Digite a segunda nota do aluno (ou -1 para encerrar): '))
    nota3 = float(input('Digite a terceira nota do aluno (ou -1 para encerrar): '))
    
    notas_menores = [nota1, nota2, nota3]
    notas_maior = max(nota1, nota2, nota3)
    
    notas_menores.remove(notas_maior)
    media = (notas_maior * 4 + sum(notas_menores) * 3) / 10
    print(f'A média ponderada do aluno é: { media }')
    if media>=5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')