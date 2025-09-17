import os,time,random #iportando funções (os para limpar a tela, time para calcular o tempo de jogo e random para o jogador aleatório)
import flet as ft
x,o = [],[]
msg = ''
inicio = time.time()
vez = ' ⭕  ' if random.randint(1, 2) else ' ❌  '
casas = {str(i): '     ' for i in range(1, 10)}
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
# def velha(msg=''):#função para mostrar o tabuleiro
#     os.system("cls" if os.name == "nt" else "clear")
#     print(f'|==Jogo=da=Velha==|')
#     print(f'|{casas['1']}|{casas['2']}|{casas['3']}|')
#     print(f'|-----+-----+-----|')
#     print(f'|{casas['4']}|{casas['5']}|{casas['6']}|')
#     print(f'|-----+-----+-----|')
#     print(f'|{casas['7']}|{casas['8']}|{casas['9']}|')
#     print(f'|=================|')
#     print(msg if msg else '')
# def venceu():#função para verificar se alguém venceu e parar o jogo
#     for a, b, c in combinacoes_vitoria:
#         if (a in x and b in x and c in x) or (a in o and b in o and c in o):
#             velha(f"{ ('⭕' if vez == ' ❌  ' else '❌')} venceu!")
#             return True
#         elif len(x) + len(o) == 9:velha("Velha!")
#  while not venceu() and len(x) + len(o) < 9:#loop principal do jogo
#      velha(msg)
#      jogada = input(f"{vez.replace(' ','')}, escolha uma casa 😉 (1-9): ")#Pedindo a jogada
#      if jogada.isnumeric() and 1 <= int(jogada) <= 9:#verificando se a jogada é valida
#          if int(jogada) in x or int(jogada) in o: msg = "⚠️ Casa já ocupada! Escolha outra."
#          else: #Trocando a vez e marcando a jogada no tabuleiro
#              (x if vez == " ❌  " else o).append(int(jogada))
#              casas[jogada] = vez
#              vez = " ⭕  " if vez == " ❌  " else " ❌  "
#              msg = ''
#      else: msg = "❌Jogada inválida! Digite um número de 1 a 9."
# print(f'⏱️A partida durou {int((time.time() - inicio) // 60)} minuto(s) e {((time.time() - inicio) % 60):.0f} segundo(s).')
def v1 (page):
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
    casa0 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa1 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa2 =  ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa3 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa4 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa5 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa6 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa7 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    casa8 = ft.OutlinedButton(' ',on_click=None,disabled=False)
    page.add(
        ft.GridView(
                    expand=True,
                    runs_count=2,
                    max_extent=150,
                    child_aspect_ratio=1,
                    spacing=20,
                    run_spacing=20,
                    controls=[casa0,casa1,casa2,casa3,casa4,casa5,casa6,casa7,casa8]
                )
    )
    
def bot(page):
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