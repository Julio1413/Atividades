chico = 1.5
chico_c=0.02

ze = 1.1
ze_c=0.03

anos = 0

while chico >= ze:
    chico += chico_c
    ze += ze_c
    anos += 1
    
print(f'Serão necessários {anos} anos para Ze ser maior que Chico.')