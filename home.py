l = []
sequencia = int(input("Digite um núero de termos para a sequência de Fibonancci"))
for i in range(0,sequencia):
    if len(l) <2: l.append(1)
    else: 
        l.append(l[i-1]+l[i-2])
print(l)