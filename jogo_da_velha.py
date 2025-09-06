import os,time,random #iportando funções (os para limpar a tela, time para calcular o tempo de jogo e random para o jogador aleatório)
x, o ,msg,inicio , vez, casas, combinacoes_vitoria = [],[],'',time.time(), '  O  ' if random.randint(1,2) else '  X  ',{str(i): '     ' for i in range(1, 10)}, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]#listas dos jogadores
def velha(msg=''):#função para mostrar o tabuleiro
    os.system("clear")
    print(f"|--Jogo-da-velha--|\n|=================|\n|{casas['1']}|{casas['2']}|{casas['3']}|\n|-----+-----+-----|\n|{casas['4']}|{casas['5']}|{casas['6']}|\n|-----+-----+-----|\n|{casas['7']}|{casas['8']}|{casas['9']}|\n|=================|")
    print(msg if msg else '')
def venceu():#função para verificar se alguém venceu e parar o jogo
    for a, b, c in combinacoes_vitoria:
        if (a in x and b in x and c in x) or (a in o and b in o and c in o):
            velha(f"{ ('O' if vez == '  X  ' else 'X')} venceu!")
            return True
        elif len(x) + len(o) == 9:velha("Velha!")
while not venceu() and len(x) + len(o) < 9:#loop principal do jogo
    velha(msg)
    jogada = input(f"{vez.replace(' ','')}, escolha uma casa (1-9): ")#Pedindo a jogada
    if jogada.isnumeric() and 1 <= int(jogada) <= 9:#verificando se a jogada é valida
        if int(jogada) in x or int(jogada) in o: msg = "Casa já ocupada! Escolha outra."
        else: #Trocando a vez e marcando a jogada no tabuleiro
            (x if vez == "  X  " else o).append(int(jogada))
            casas[jogada] = vez
            vez = "  O  " if vez == "  X  " else "  X  "
            msg = ''
    else: msg = "Jogada inválida! Digite um número de 1 a 9."
print(f'A partida durou {int((time.time() - inicio) // 60)} minuto(s) e {((time.time() - inicio) % 60):.0f} segundo(s).')