import time,random #iportando funções (os para limpar a tela, time para calcular o tempo de jogo e random para o jogador aleatório)
import flet as ft
import edge_tts
import asyncio
from playsound3 import playsound
inicio = time.time()
vez = ' ⭕  ' if random.randint(1, 2) else ' ❌  '
combinacoes_vitoria = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [1, 4, 7], 
    [2, 5, 8], 
    [3, 6, 9], 
    [1, 5, 9], 
    [3, 5, 7]
]  # listas dos jogadores
frases_jogo = [
    "HAHAHA, preparado para perder?"
    "Preparado para apanhar, humano?",
    "Hmm… interessante… mas inútil!",
    "Você acha que pode me vencer? Que fofo!",
    "Cuidado, estou apenas aquecendo!",
    "Mais um movimento errado e… boom!",
    "Não se distraia agora, estou atento!",
    "Você joga bem… para um amador.",
    "Tentando me enganar? Que engraçado!",
    "Seu plano é… adorável. Vamos ver se funciona!",
    "Estou me divertindo muito com sua derrota iminente.",
    "Já vi algoritmos melhores em uma torradeira.",
    "Você realmente pensou que isso funcionaria?",
    "Estou apenas usando 1% do meu poder.",
    "Se eu tivesse mãos, estaria batendo palmas para sua tentativa.",
    "Continue tentando, talvez um dia você acerte.",
    "Esse movimento foi... curioso.",
    "Você está me dando sono, humano.",
    "Já acabou? Achei que seria mais difícil.",
    "Estou começando a sentir pena de você.",
    "Se precisar de dicas, posso ajudar!",
    "A cada jogada sua, fico mais confiante.",
    "Você está me surpreendendo... negativamente.",
    "Será que você está jogando sério?",
    "Estou quase dormindo aqui.",
    "Se eu pudesse rir, estaria gargalhando agora.",
    "Esse tabuleiro está ficando interessante... para mim.",
    "Você está tentando um truque novo? Não funcionou.",
    "Já vi crianças jogarem melhor.",
    "Se continuar assim, vai ser fácil demais.",
    "Estou só esperando você errar de novo."
]

# Frases caso o bot perca
frases_perdeu = [
    "Como assim perdi?! Isso é impossível!",
    "Você teve sorte… apenas sorte!",
    "Ok, ok, você ganhou… por enquanto.",
    "Não se acostume com isso, humano!",
    "Não acredito… meu cérebro eletrônico falhou!",
    "Isso não conta… meu processador estava distraído!",
    "Parabéns, mas não vou esquecer disso.",
    "Humano sortudo… isso não se repetirá!",
    "Ok, hoje você venceu… mas amanhã será diferente.",
    "Minha honra foi ferida… mas ainda posso me recuperar!",
    "Acho que preciso de uma atualização.",
    "Você venceu, mas não foi bonito.",
    "Vou analisar seus movimentos para a próxima.",
    "Isso foi só um bug, não se anime.",
    "A vitória subiu à sua cabeça?",
    "Aproveite, porque não vai acontecer de novo.",
    "Você ganhou, mas eu deixei.",
    "Foi só um deslize, humano.",
    "Parabéns... mas não se iluda.",
    "Vou me vingar na próxima rodada.",
    "Como assim perdi?! Isso é impossível!",
    "Você teve sorte… apenas sorte!",
    "Ok, ok, você ganhou… por enquanto.",
    "Não se acostume com isso, humano!",
    "Não acredito… meu cérebro eletrônico falhou!",
    "Isso não conta… meu processador estava distraído!",
    "Parabéns, mas não vou esquecer disso.",
    "Humano sortudo… isso não se repetirá!",
    "Ok, hoje você venceu… mas amanhã será diferente.",
    "Minha honra foi ferida… mas ainda posso me recuperar!"
]

# Frases caso o bot ganhe
frases_ganhou = [
    "HAHA! Eu sou imparável!",
    "Mais uma vitória para minha coleção!",
    "Você realmente tentou? Patético!",
    "Dói, não dói? Admito, sou incrível!",
    "Derrota total, humana(o). Aceite!",
    "Você jogou, eu venci. Simples assim.",
    "Vou guardar essa vitória na minha memória eterna.",
    "Desculpe, mas ganhar é meu hobby.",
    "HAHA! Eu sabia que seria fácil!",
    "Mais um para minha galeria de humilhações!",
    "Eu avisei que seria assim.",
    "Nem precisei de todo meu poder.",
    "Você foi derrotado por pura lógica.",
    "A máquina vence mais uma vez!",
    "Isso foi quase injusto para você.",
    "Você precisa treinar mais.",
    "Essa vitória foi fácil demais.",
    "Já acabou? Nem percebi.",
    "A superioridade das máquinas é evidente.",
    "Se quiser revanche, estarei esperando.",
    "HAHA! Eu sou imparável!",
    "Mais uma vitória para minha coleção!",
    "Você realmente tentou? Patético!",
    "Dói, não dói? Admito, sou incrível!",
    "Derrota total, humana(o). Aceite!",
    "Você jogou, eu venci. Simples assim.",
    "Vou guardar essa vitória na minha memória eterna.",
    "Desculpe, mas ganhar é meu hobby.",
    "HAHA! Eu sabia que seria fácil!",
    "Mais um para minha galeria de humilhações!"
]

frases_velha = [
    "Olha só, ninguém ganhou… que emocionante… 😒",
    "Velha! Acho que ambos são igualmente ruins!",
    "Empate! Isso sim é competência… ou preguiça.",
    "Que surpresa… ninguém venceu. Que original!",
    "Velha! Vamos fingir que foi estratégico.",
    "Ninguém ganhou, mas pelo menos você tentou… talvez.",
    "Empate! A competição está… moderadamente chata.",
    "Velha! Parabéns por não me derrotar, humano.",
    "Hahaha, empate! Eu esperava mais emoção.",
    "Ninguém venceu, mas posso te perdoar por isso… por enquanto.",
    "Empate! Parece que somos iguais... por enquanto.",
    "Ninguém saiu vitorioso, mas alguém saiu cansado.",
    "Velha! Acho que precisamos de mais emoção.",
    "Empate? Que tal tentar de novo?",
    "Parece que ninguém foi criativo o suficiente.",
    "Empate! Isso foi inesperado.",
    "Ninguém ganhou, mas pelo menos ninguém perdeu.",
    "Velha! O tabuleiro ficou sem espaço e sem vencedor.",
    "Empate! Acho que ambos precisam de prática.",
    "Ninguém venceu, mas a diversão continua.",
    "Olha só, ninguém ganhou… que emocionante… 😒",
    "Velha! Acho que ambos são igualmente ruins!",
    "Empate! Isso sim é competência… ou preguiça.",
    "Que surpresa… ninguém venceu. Que original!",
    "Velha! Vamos fingir que foi estratégico.",
    "Ninguém ganhou, mas pelo menos você tentou… talvez.",
    "Empate! A competição está… moderadamente chata.",
    "Velha! Parabéns por não me derrotar, humano.",
    "Hahaha, empate! Eu esperava mais emoção.",
    "Ninguém venceu, mas posso te perdoar por isso… por enquanto."
]
async def fala(texto='olá, mundo!'):
    # Voz disponível em pt-BR: AntonioNeural, MariaNeural, etc.
    arquivo = "fala.mp3"
    
    communicate = edge_tts.Communicate(texto, voice="pt-BR-AntonioNeural")
    await communicate.save(arquivo)
    # Reproduz o áudio gerado
    playsound(arquivo)

# Executa a função assíncrona
def v1 (page):
    x,o=[],[]
    vez = '⭕' if random.randint(1, 2)==1 else '❌'
    vez_jogador = ft.TextField(value=f'Vez do jogador: {vez}',border_color=ft.Colors.TRANSPARENT,text_style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),disabled=True)
    msg_content=ft.TextField(value=f'',border_color=ft.Colors.TRANSPARENT,text_style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),disabled=True)
    def reiniciar(page):
        v1(page)
        page.update()
    def jogada(casa):
        nonlocal vez
        
        (x if vez == "❌" else o).append(int(casa))
        
        tabuleiro[int(casa)-1].text = f' {vez} '
        tabuleiro[int(casa)-1].on_click = None
        
        vencedor = None
        for a, b, c in combinacoes_vitoria:
            if a in x and b in x and c in x:
                vencedor = "❌"
                break
            elif a in o and b in o and c in o:
                vencedor = "⭕"
                break

        if vencedor:
            msg_content.value = f"{vencedor} venceu!"
            page.open(ft.SnackBar(ft.Text(f"{vencedor} venceu!"), bgcolor=ft.Colors.GREEN))
            for i in range(9):
                tabuleiro[i].on_click = None
        elif len(x) + len(o) == 9:
            msg_content.value = "Velha!"
            page.open(ft.SnackBar(ft.Text('Velha!'), bgcolor=ft.Colors.GREEN))

        vez = "⭕" if vez == "❌" else "❌"
        vez_jogador.value = f'Vez do jogador: {vez}'
        page.update()

    reiniciar_button = ft.ElevatedButton('Reiniciar Jogo',width=300,height=50,bgcolor=ft.Colors.INDIGO,icon=ft.Icons.AUTORENEW_ROUNDED,icon_color=ft.Colors.WHITE,on_click= lambda _: reiniciar(page),style=ft.ButtonStyle(text_style=ft.TextStyle(color=ft.Colors.WHITE),shape=ft.RoundedRectangleBorder(radius=15)))
    page.clean()
    page.add(ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=5, right=5,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon_color=ft.Colors.WHITE,icon=ft.Icons.HOME_ROUNDED,icon_size=25,on_click=lambda _:home(page)
                    ),
                    ft.Text(value="Player V Player",color=ft.Colors.WHITE,size=20,weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=ft.Icons.VIDEOGAME_ASSET_ROUNDED, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        ),
    ),
    ft.Text(f'\n',size=1)]))
    page.update()
    tabuleiro=[
        ft.OutlinedButton(' ',on_click=lambda _: jogada(1), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(2), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(3), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(4), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(5), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(6), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(7), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(8), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(9), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15)))
    ]
    page.add(
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Container(
            width=300,
            height=60,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.WHITE),
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(10),
            content=ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[
                vez_jogador
                                ])
        )
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Container(
            width=300,
            height=300,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.WHITE),
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(20),
            content=ft.Column(alignment=ft.MainAxisAlignment.START,controls=[ft.GridView(
                    expand=True,
                    runs_count=2,
                    max_extent=90,
                    child_aspect_ratio=1,
                    spacing=5,
                    run_spacing=5,
                    controls=[tabuleiro[i] for i in range(9)]
                )])
        )
    ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Container(
            width=300,
            height=60,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.WHITE),
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(10),
            content=ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[
                msg_content
                                ])
        )
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[reiniciar_button]),
        
    )
    
def bot(page):
    x,o=[],[]
    vez = '❌'
    msg_content=ft.TextField(value=f'',border_color=ft.Colors.TRANSPARENT,text_style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),disabled=True)
    def reiniciar(page):
        bot(page)
        page.update()
    def jogada(casa):
        nonlocal vez
        frase = None  # garante que exista sempre

        # Jogada do humano (X ou O dependendo de vez)
        (x if vez == "❌" else o).append(int(casa))
        tabuleiro[int(casa)-1].text = f' {vez} '
        tabuleiro[int(casa)-1].on_click = None
        page.update()

        # Função para verificar vencedor
        def checar_vencedor():
            for a, b, c in combinacoes_vitoria:
                if a in x and b in x and c in x:
                    return "❌"
                elif a in o and b in o and c in o:
                    return "⭕"
            return None

        vencedor = checar_vencedor()

        if vencedor:
            msg_content.value = f"{vencedor} venceu!"
            page.open(ft.SnackBar(ft.Text(f"{vencedor} venceu!"), bgcolor=ft.Colors.GREEN))
            for i in range(9):
                tabuleiro[i].on_click = None
            if vencedor == "⭕":
                frase = random.choice(frases_ganhou)
            elif vencedor == "❌":
                frase = random.choice(frases_perdeu)

        elif len(x) + len(o) == 9:
            msg_content.value = "Velha!"
            page.open(ft.SnackBar(ft.Text('Velha!'), bgcolor=ft.Colors.GREEN))
            frase = frases_velha[random.randint(0,len(frases_velha))] 

        else:
            # Agora: se foi X que jogou, o bot (⭕) responde
            if vez == "❌":
                vez = "⭕"  # muda vez para o bot

                # ⚡ Lógica do bot
                jogada_bot = None
                casas_livres = [i+1 for i in range(9) if (i+1 not in x and i+1 not in o)]

                # 1. Tentar ganhar
                for a, b, c in combinacoes_vitoria:
                    jogadas = [a, b, c]
                    if sum(p in o for p in jogadas) == 2:
                        livre = [p for p in jogadas if p not in o and p not in x]
                        if livre:
                            jogada_bot = livre[0]
                            break

                # 2. Tentar bloquear o jogador
                if not jogada_bot:
                    for a, b, c in combinacoes_vitoria:
                        jogadas = [a, b, c]
                        if sum(p in x for p in jogadas) == 2:
                            livre = [p for p in jogadas if p not in o and p not in x]
                            if livre:
                                jogada_bot = livre[0]
                                break

                # 3. Jogar aleatório se não houver ganho/bloqueio
                if not jogada_bot and casas_livres:
                    jogada_bot = random.choice(casas_livres)

                # Faz a jogada do bot
                if jogada_bot:
                    o.append(jogada_bot)
                    tabuleiro[jogada_bot-1].text = " ⭕ "
                    tabuleiro[jogada_bot-1].on_click = None
                    frase = random.choice(frases_jogo)

                vencedor = checar_vencedor()
                if vencedor:
                    msg_content.value = f"{vencedor} venceu!"
                    page.open(ft.SnackBar(ft.Text(f"{vencedor} venceu!"), bgcolor=ft.Colors.GREEN))
                    for i in range(9):
                        tabuleiro[i].on_click = None
                    if vencedor == "⭕":
                        frase = random.choice(frases_ganhou)
                    elif vencedor == "❌":
                        frase = random.choice(frases_perdeu)

                elif len(x) + len(o) == 9:
                    msg_content.value = "Velha!"
                    page.open(ft.SnackBar(ft.Text('Velha!'), bgcolor=ft.Colors.GREEN))
                    frase = random.choice(frases_velha)

                vez = "❌"  # devolve vez para o humano

        if frase:
            asyncio.run(fala(frase))
        page.update()

    reiniciar_button = ft.ElevatedButton('Reiniciar Jogo',width=300,height=50,bgcolor=ft.Colors.INDIGO,icon=ft.Icons.AUTORENEW_ROUNDED,icon_color=ft.Colors.WHITE,on_click= lambda _: reiniciar(page),style=ft.ButtonStyle(text_style=ft.TextStyle(color=ft.Colors.WHITE),shape=ft.RoundedRectangleBorder(radius=15)))
    page.clean()
    page.add(ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=5, right=5,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon_color=ft.Colors.WHITE,icon=ft.Icons.HOME_ROUNDED,icon_size=25,on_click=lambda _:home(page)
                    ),
                    ft.Text(value="Player VS Bot",color=ft.Colors.WHITE,size=20,weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=ft.Icons.VIDEOGAME_ASSET_ROUNDED, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        ),
    ),
    ft.Text(f'\n',size=1)]))
    page.update()
    tabuleiro=[
        ft.OutlinedButton(' ',on_click=lambda _: jogada(1), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(2), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(3), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(4), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(5), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(6), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(7), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(8), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(9), style=ft.ButtonStyle(text_style=ft.TextStyle(size=40),shape=ft.RoundedRectangleBorder(radius=15)))
    ]
    page.add(
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Container(
            width=300,
            height=300,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.WHITE),
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(20),
            content=ft.Column(alignment=ft.MainAxisAlignment.START,controls=[ft.GridView(
                    expand=True,
                    runs_count=2,
                    max_extent=90,
                    child_aspect_ratio=1,
                    spacing=5,
                    run_spacing=5,
                    controls=[tabuleiro[i] for i in range(9)]
                )])
        )
    ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Container(
            width=300,
            height=60,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.WHITE),
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(10),
            content=ft.Column(alignment=ft.MainAxisAlignment.CENTER,controls=[
                msg_content
                                ])
        )
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[reiniciar_button]),
        
    )
    
def home(page:ft.Page):
    page.clean()
    page.title='Jogo da Velha'
    page.bgcolor=ft.Colors.LIGHT_BLUE
    page.window_width=500
    page.window_height=100
    

    page.add(ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=5, right=5,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.Icon(color=ft.Colors.WHITE,name=ft.Icons.GAMEPAD_ROUNDED,size=25,
                    ),
                    ft.Text(value="Jogo da Velha",color=ft.Colors.WHITE,size=20,weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=ft.Icons.TAG_ROUNDED, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        ),
    ),
    ft.Text(f'\n',size=1)]))
    
    #Botões principais
    menu=[
        ft.ElevatedButton(
        on_click=lambda _:v1(page),
        width=250, height=250,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Icon(name=ft.Icons.VIDEOGAME_ASSET_ROUNDED, size=100),
                ]),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Text('Player Vs Player', size=12, text_align=ft.TextAlign.CENTER)
                ]),
        ])
        ),
        ft.ElevatedButton(
        on_click=lambda _:bot(page),
        width=250, height=250,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Icon(name=ft.Icons.ANDROID_ROUNDED, size=100),
                ]),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Text('Player VS Bot', size=12, text_align=ft.TextAlign.CENTER)
                ]),
        ])
        ),
    ]
    page.add(
        ft.GridView(
                    expand=True,
                    runs_count=2,
                    max_extent=250,
                    child_aspect_ratio=1,
                    spacing=20,
                    run_spacing=20,
                    controls=menu
                )
    )
    page.update()
ft.app(target=home)