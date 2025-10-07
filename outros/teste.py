def inverter (string):
    saida=''
    string = string.split()
    for palavra in string:
        saida=f'{palavra} '+saida
    return saida
string = str(input('Digite uma frase grande: '))
print(inverter(string))