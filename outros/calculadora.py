n1 = (input('Digite um número para fazer a operação: '))
n2 = (input('Digite outro número para fazer a operação: '))
op = input('Digite uma operação (+,/,*,-):')
if (str(n1).replace('.','')+str(n2).replace('.','')+str(n1).replace(',','')+str(n2).replace(',','')).isnumeric() and op in '+/*-':
    if op =='+':print(float(n1.replace(',','.'))+float(n2.replace(',','.')))
    elif op =='-':print(float(n1.replace(',','.'))-float(n2.replace(',','.')))
    elif op =='/':print(float(n1.replace(',','.'))/float(n2.replace(',','.')))
    elif op=='*':print(float(n1.replace(',','.'))*float(n2.replace(',','.')))
else: print('Digite uma operação válida!!')