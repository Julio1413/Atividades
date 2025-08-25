#iportando funções (os para limpar a tela e time para calcular o tempo de jogo)
import os
import time
#listas dos jogadores
x = []
o = []
vez = "  X  "
msg = ''
#dicionário das casas do jogo
casas = {str(i): '     ' for i in range(1, 10)}
#combinações de vitória
combinacoes_vitoria = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
#função para mostrar o tabuleiro
def velha(msg=''):
    os.system("cls")
    print(f"|--Jogo-da-velha--|")
    print(f"|=================|")
    print(f"|{casas['1']}|{casas['2']}|{casas['3']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['4']}|{casas['5']}|{casas['6']}|")
    print(f"|-----+-----+-----|")
    print(f"|{casas['7']}|{casas['8']}|{casas['9']}|")
    print(f"|=================|")
    if msg:
        print(msg)
#função para verificar se alguém venceu e parar o jogo
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
#loop principal do jogo
inicio = time.time()
while not venceu():
    velha(msg)
    #Pedindo a jogada
    jogada = input(f"{vez.replace(' ','')}, escolha uma casa (1-9): ")
    #verificando se a jogada é valida
    if jogada.isnumeric() and 1 <= int(jogada) <= 9:
        if int(jogada) in x or int(jogada) in o: msg = "Casa já ocupada! Escolha outra."
        else:
            #Trocando a vez e marcando a jogada no tabuleiro
            if vez == "  X  ":
                x.append(int(jogada))
                casas[jogada] = vez
                vez = "  O  "
            else:
                o.append(int(jogada))
                casas[jogada] = vez
                vez = "  X  "
            msg = ''
    else: msg = "Jogada inválida! Digite um número de 1 a 9."
print(f'A partida durou {int((time.time() - inicio) // 60)} minuto(s) e {((time.time() - inicio) % 60):.2f} segundo(s).')