import os
x = []
o = []
vez = "  X  "
msg = ''
casas = {str(i): '     ' for i in range(1, 10)}  # só de 1 a 9
combinacoes_vitoria = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
def velha(msg=''):
    os.system("clear")
    print(f"o--Jogo-da-velha--O")
    print(f"|=================|")
    print(f"|{casas['1']}|{casas['2']}|{casas['3']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['4']}|{casas['5']}|{casas['6']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['7']}|{casas['8']}|{casas['9']}|")
    print(f"o=================o")
    if msg:
        print(msg)
def venceu():
    for a, b, c in combinacoes_vitoria:
        if a in x and b in x and c in x:
            velha("X venceu!")
            return True
        elif a in o and b in o and c in o:
            velha("O venceu!")
            return True
    if len(x) + len(o) == 9:
        velha("Velha!")
        return True
    return False
while not venceu():
    velha(msg)
    jogada = input(f"{vez}, escolha uma casa (1-9): ")
    if jogada.isnumeric() and 1 <= int(jogada) <= 9:
        if int(jogada) in x or int(jogada) in o:
            msg = "Casa já ocupada! Escolha outra."
        else:
            if vez == "  X  ":
                x.append(int(jogada))
                casas[jogada] = vez
                vez = "  O  "
            else:
                o.append(int(jogada))
                casas[jogada] = vez
                vez = "  X  "
            msg = ''
    else:
        msg = "Jogada inválida! Digite um número de 1 a 9."