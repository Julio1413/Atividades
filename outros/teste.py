def inverter (string):
    saida=''
    for palavra in string.split():saida=f'{palavra} '+saida
    return saida
string = str(input('Digite uma frase grande: '))
print(inverter(string))