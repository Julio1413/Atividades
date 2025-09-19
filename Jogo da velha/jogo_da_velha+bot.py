import os,time,random #iportando funções (os para limpar a tela, time para calcular o tempo de jogo e random para o jogador aleatório)
import flet as ft

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
def v1 (page):
    x,o=[],[]
    vez = '⭕' if random.randint(1, 2)==1 else '❌'
    def reiniciar(page):
        v1(page)
        page.update()
    def jogada(casa):
        nonlocal vez
        (x if vez == "❌" else o).append(int(casa))
        tabuleiro[int(casa)].text = f' {vez} '
        tabuleiro[int(casa)].on_click = None
        vez = "⭕" if vez == "❌" else "❌"
        page.update()
    reiniciar_button = ft.ElevatedButton('Reiniciar Jogo',width=300,height=50,bgcolor=ft.Colors.INDIGO,icon=ft.Icons.AUTORENEW_ROUNDED,icon_color=ft.Colors.WHITE,on_click= lambda _: reiniciar(page),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)))
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
        ft.OutlinedButton(' ',on_click=lambda _: jogada(0), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(1), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(2), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(3), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(4), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(5), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(6), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(7), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))),
        ft.OutlinedButton(' ',on_click=lambda _: jogada(i), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)))
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
                ft.Text(f'Vez do jogador: {vez}',size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)
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
        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[reiniciar_button]),
        
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