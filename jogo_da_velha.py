import os,time,random #iportando funções (os para limpar a tela, time para calcular o tempo de jogo e random para o jogador aleatório)
x, o ,msg = [],[],''#listas dos jogadores
if random.randint(1,2)==1: vez = "  X  "
else: vez = "  O  "
casas = {str(i): '     ' for i in range(1, 10)}#dicionário das casas do jogo
combinacoes_vitoria = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]#combinações de vitória
def printar(pnt=''):print(pnt if pnt else '')
def velha():#função para mostrar o tabuleiro
    os.system("clear")
    print(f"|--Jogo-da-velha--|\n|=================|\n|{casas['1']}|{casas['2']}|{casas['3']}|\n|-----+-----+-----|\n|{casas['4']}|{casas['5']}|{casas['6']}|\n|-----+-----+-----|\n|{casas['7']}|{casas['8']}|{casas['9']}|\n|=================|")
def venceu():#função para verificar se alguém venceu e parar o jogo
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
inicio = time.time()
while not venceu():
    velha()
    printar(msg)
    jogada = input(f"{vez.replace(' ','')}, escolha uma casa (1-9): ")#Pedindo a jogada
    if jogada.isnumeric() and 1 <= int(jogada) <= 9:#verificando se a jogada é valida
        if int(jogada) in x or int(jogada) in o: msg = "Casa já ocupada! Escolha outra."
        else: #Trocando a vez e marcando a jogada no tabuleiro
            lista = x if vez == "  X  " else o
            lista.append(int(jogada))
            casas[jogada] = vez
            vez = "  O  " if vez == "  X  " else "  X  "
            msg = ''
    else: msg = "Jogada inválida! Digite um número de 1 a 9."
print(f'A partida durou {int((time.time() - inicio) // 60)} minuto(s) e {((time.time() - inicio) % 60):.0f} segundo(s).')