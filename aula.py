l=[]
while True:
    n = int(input('Digite um número (digite 0 para sair): '))
    if n!=0: l.append(n)
    else: break
    print(l)
    
n=int(input('Digite um número para verificar e está presente:'))
if n in l:print('Está presente!')
else:print('Não está presente!')
 
n=int(input('Digite algo pra remover'))
for i in l:
    if l[f'{i}']==n:l.remove(n)