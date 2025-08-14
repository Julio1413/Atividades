import os
x=[]
o=[]
vez ="  X  "
casas = {"1":"     ","2":"     ","3":"     ","4":"     ","5":"     ","6":"     ","7":"     ","8":"     ","9":"     "}
combinacoes_vitoria = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
def velha():
    os.system("clear")
    print(f"o--Jogo-da-velha--o")
    print(f"|=================|")
    print(f"|{casas['1']}|{casas['2']}|{casas['3']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['4']}|{casas['5']}|{casas['6']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['7']}|{casas['8']}|{casas['9']}|")
    print(f"o=================o")
def venceu():
        for a,b,c in combinacoes_vitoria:
            if a in x and b in x and c in x:
                velha()
                print("X venceu!")
                return True
            elif a in o and b in o and c in o:
                velha()
                print("O venceu!")
                return True
        if len(x) + len(o) == 9:
            velha()
            print("Velha!")
            return True
        return False
while venceu()==False:    
    velha()
    jogada = str(input(f"{vez}, escolha uma casa:\n(1-9) "))
    if not jogada in '123456789':
        print("Jogada inválida! Escolha um número entre 1 e 9.")
    else:
        if int(jogada) in x or int(jogada) in o:
            print("Casa já ocupada! Escolha outra casa.")
        else:
            if vez == "  X  ":
                x.append(int(jogada))
                casas[f"{int(jogada)}"] = vez
                vez = "  O  "
            else:
                o.append(int(jogada))
                casas[f"{int(jogada)}"] = vez
                vez = "  X  "
    venceu()