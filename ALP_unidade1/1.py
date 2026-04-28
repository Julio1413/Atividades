l=[]
for i in range(5):
    a = float(input(f'Digite {6-1} e saberás quantos são negativos'))
    l.append(a)
negativos = 0
for i in l:
    if i <0:
        negativos +=1
print(f'{negativos} são negativos!')
