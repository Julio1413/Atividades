import flet as ft
import os
import random
from time import sleep, time
from playsound3 import playsound
from edge_tts import Communicate
from asyncio import run
from difflib import SequenceMatcher

with open('perguntas.txt','r', encoding="utf-8") as f:
    perguntas_l = f.readlines()
with open('respostas.txt','r', encoding="utf-8") as f:
    respostas_l = f.readlines()
respostas_l = [resposta.replace('\n','') for resposta in respostas_l]
perguntas_l = [pergunta if pergunta.endswith('\n') else pergunta+'\n' for pergunta in perguntas_l]
print(perguntas_l)
print(respostas_l)

def exibir_resultados(page,acertos_l,perguntas_jogadas,perguntas_player,tempo,tempo_individual):
    print(tempo_individual)
    page.add(
            ft.Column(
                controls=[
                    ft.Container(
                        height=90,
                        content=ft.Container(
                            alignment=ft.alignment.bottom_center,
                            padding=ft.padding.only(left=10, right=10, bottom=10),
                            blur=(10, 10),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.Colors.WHITE,
                                        icon_size=30,
                                        on_click=lambda _: main(page)
                                    ),
                                    ft.Text(
                                        value="Resultados do Quiz",
                                        color=ft.Colors.WHITE,
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Icon(
                                        name=ft.Icons.QUIZ_ROUNDED,
                                        color=ft.Colors.WHITE,
                                        size=30,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            height=50,
                        ),
                    ),
                ]
            )
        )
    tela_respostas = []
    for i in range(len(perguntas_jogadas)):
        indice = perguntas_jogadas[i]
        tela_respostas.append(ft.Container(
                expand=True,
                padding=ft.Padding(top=10,right=10,left=10,bottom=10),
                bgcolor=ft.Colors.WHITE,
                border_radius=ft.border_radius.all(16),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                    controls=[
                        ft.Text(f'Pergunta {i+1}: {perguntas_l[indice].strip()}',weight=ft.FontWeight.BOLD),
                        ft.Text(f'Sua resposta: {perguntas_player[i]}',weight=ft.FontWeight.W_600),
                        ft.Text(f'Resposta correta: {respostas_l[indice].strip()}',weight=ft.FontWeight.W_600),
                        ft.Text(f'Resultado: {"✅ Acertou!" if acertos_l[i]==1 else "❌ Errou!"}',weight=ft.FontWeight.W_600,color=ft.Colors.GREEN if acertos_l[i]==1 else ft.Colors.RED),
                        ft.Text(f'Tempo: {int(tempo_individual[i] // 60)} minuto(s) e {(tempo_individual[i] % 60):.0f} segundo(s)',weight=ft.FontWeight.W_600),
                        ft.Divider(),
                    ]
                )))
    page.add(
        ft.Container(
            expand=True,
            padding=ft.Padding(top=15,right=15,left=15,bottom=15),
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.all(16),
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                alignment=ft.MainAxisAlignment.START,
                expand=True,
                controls=[
                    #Título
                    ft.Text('Extatísticas',weight=ft.FontWeight.BOLD,size=20),
                    ft.Divider(),
                    ft.Text(f'Acertos: {acertos_l.count(1)}/{len(perguntas_jogadas)}',weight=ft.FontWeight.W_600),
                    ft.Text(f'Tempo total: {int(tempo // 60)} minuto(s) e {(tempo % 60):.0f} segundo(s)',weight=ft.FontWeight.W_600),
                    ft.Divider(),
                    ft.ExpansionTile(
                        title=ft.Text("Perguntas e respostas detalhadas",weight=ft.FontWeight.BOLD,size=16),
                        affinity=ft.TileAffinity.LEADING,
                        initially_expanded=False,
                        controls=tela_respostas,
                    ),
                ]
            )
        )
    )

    
def perguntas(page, quantidade_perguntas,permissao_voz):
    async def som(texto):
        audio_tts = Communicate(texto, "pt-BR-AntonioNeural")
        arquivo = "temp_audio.mp3"
        await audio_tts.save(arquivo)
        playsound(arquivo)
        os.remove(arquivo)
    sleep(0.05)
    n_perguntas_jogadas = 1
    barra_progresso = ft.ProgressBar(
        border_radius=ft.border_radius.all(10),
        width=page.width,
        height=10,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLUE_ACCENT_700,
        value=n_perguntas_jogadas / quantidade_perguntas
    )
    tempo = time()
    tempo_individual = []
    acertos_l = []
    perguntas_jogadas = []
    perguntas_player = []

    def retornar_indice():
        indice = random.randint(0, len(perguntas_l) - 1)
        while indice in perguntas_jogadas:
            indice = random.randint(0, len(perguntas_l) - 1)
        return indice

    def exibir_pergunta(i):
        nonlocal n_perguntas_jogadas

        indice_selecionado = retornar_indice()
        perguntas_jogadas.append(indice_selecionado)

        inicio_quiz = time()

        page.clean()
        page.scrollable = ft.ScrollMode.ALWAYS

        page.add(
            ft.Column(
                controls=[
                    ft.Container(
                        height=90,
                        content=ft.Container(
                            alignment=ft.alignment.bottom_center,
                            padding=ft.padding.only(left=10, right=10, bottom=10),
                            blur=(10, 10),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                        icon_color=ft.Colors.WHITE,
                                        icon_size=30,
                                        on_click=lambda _: main(page)
                                    ),
                                    ft.Text(
                                        value="Quiz 6X2",
                                        color=ft.Colors.WHITE,
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Icon(
                                        name=ft.Icons.QUIZ_ROUNDED,
                                        color=ft.Colors.WHITE,
                                        size=30,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            height=50,
                        ),
                    ),
                ]
            )
        )

        page.add(ft.Text(f"Pergunta {i} de {quantidade_perguntas}:", color=ft.Colors.WHITE, size=17, weight=ft.FontWeight.BOLD))
        page.add(barra_progresso)

        page.add(
            ft.Container(
                height=page.height*0.25,
                bgcolor=ft.Colors.WHITE,
                border_radius=ft.border_radius.all(10),
                padding=ft.padding.all(10),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            fit=ft.ImageFit.COVER,
                            src="https://i.postimg.cc/YqBv7Rw8/c1495305-3dbd-4261-9199-9f084ffe1f9d.png",
                            border_radius=ft.border_radius.all(10),
                        )
                    ],
                ),
            )
        )

        resposta_tela = ft.TextField(label="Resposta:", border_color=ft.Colors.TRANSPARENT,expand=True)


        def verificar_resposta(resposta):
            nonlocal n_perguntas_jogadas
            semelhanca = SequenceMatcher(None, respostas_l[indice_selecionado].replace('\n','').lower(), resposta.replace('\n','').lower()).ratio()
            print(semelhanca)

            tempo_i = time() - inicio_quiz
            tempo_individual.append(tempo_i)

            if semelhanca >= 0.55:
                acertos_l.append(1)
                page.open(ft.SnackBar(ft.Text("Resposta correta!"), bgcolor=ft.Colors.GREEN))
            else:
                acertos_l.append(0)
                page.open(ft.SnackBar(ft.Text("Resposta incorreta!"), bgcolor=ft.Colors.RED))

            perguntas_player.append(resposta)

            # Atualiza contador e barra de progresso depois de registrar a resposta
            n_perguntas_jogadas += 1
            barra_progresso.value = n_perguntas_jogadas / quantidade_perguntas
            page.update()

            # Avança para a próxima pergunta
            if n_perguntas_jogadas <= quantidade_perguntas:
                exibir_pergunta(n_perguntas_jogadas)
            else:
                page.clean()
                exibir_resultados(page,acertos_l,perguntas_jogadas,perguntas_player,time() - tempo,tempo_individual)
                page.update()

        page.add(
            ft.Container(
                expand=True,
                width=page.width,
                padding=ft.padding.all(10),
                bgcolor=ft.Colors.WHITE,
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text(f"{perguntas_l[indice_selecionado].strip()}", weight=ft.FontWeight.BOLD, size=13),
                        ft.Divider(),
                        resposta_tela,
                        ft.Divider(),
                        ft.ElevatedButton(
                            text="Enviar Resposta",
                            icon=ft.Icons.SEND_ROUNDED,
                            on_click=lambda e: verificar_resposta(resposta_tela.value),
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_ACCENT_700,
                            width=page.width,
                        ),
                    ],
                ),
            )
        )
        if permissao_voz:run(som(perguntas_l[indice_selecionado].replace('\n','')))

    # Mostra a primeira pergunta
    exibir_pergunta(1)
    
def editar_perguntas(page):
# Função para editar as perguntas
    def save_files():
        # Salva as perguntas e respostas
        # salva as listas atuais nos arquivos para persistência
        
        with open('perguntas.txt', 'w', encoding='utf-8') as f:
            f.writelines(perguntas_l)
        with open('respostas.txt', 'w', encoding='utf-8') as f:
            f.writelines(respostas_l)

    def excluir_pergunta(n_linha):
        # Exclui uma pergunta
        # remove a pergunta e resposta pelo índice, salva e recarrega a interface
        if 0 <= n_linha < len(perguntas_l):
            perguntas_l.pop(n_linha)
            respostas_l.pop(n_linha)
            save_files()
            editar_perguntas(page)
    page.clean()
    page.update()
    page.scroll = ft.ScrollMode.ALWAYS
    def adicionar_dialog(page):
        # Adiciona uma nova pergunta
        nova_pergunta = ft.TextField(label='Nova pergunta:',hint_text=random.choice(perguntas_l))
        nova_resposta = ft.TextField(label='Nova resposta:',hint_text=random.choice(respostas_l))

        def close_dlg(e=None):
            dlg.open = False
            page.update()

        def add_p(e=None):
            pergunta = nova_pergunta.value.strip()
            resposta = nova_resposta.value.strip()
            if pergunta and resposta:
                if len(perguntas_l) ==50:
                    page.open(ft.SnackBar(content=ft.Text('Número máximo de perguntas atingido (50)!'),bgcolor=ft.Colors.RED))
                    page.update()
                else:
                    perguntas_l.append(f'\n{pergunta}')
                    respostas_l.append(f'\n{resposta}')
                    close_dlg()
                    save_files()
                    editar_perguntas(page)
                    page.update()
            else:
                page.open(ft.SnackBar(content=ft.Text('Preencha todos os campos!'),bgcolor=ft.Colors.RED))
                page.update()

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text('Adicionar nova questão', weight=ft.FontWeight.BOLD, size=20),
            content=ft.Column(
                controls=[
                    ft.Text('(Certifique-se de adicionar a resposta também!)', size=15),
                    nova_pergunta,
                    nova_resposta,
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Image(width=300,height=300,src='https://i.pinimg.com/736x/12/d3/fd/12d3fd7fb251029749a0ae762159f21b.jpg',expand=True,border_radius=ft.border_radius.all(10))])
                    
                ]
            ),
            actions=[
                ft.TextButton("Adicionar", on_click=add_p),
                ft.TextButton("Cancelar", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.open(dlg)
        page.update()
    def chamar_main(e=None):
        page.clean()
        page.update()
        main(page)
    page.add(
        ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=10, right=10,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                                icon=ft.Icons.ARROW_BACK_IOS_NEW_OUTLINED,
                                icon_color=ft.Colors.WHITE,
                                icon_size=30,
                                on_click=lambda e: chamar_main()
                            ),
                    ft.Text(
                        value='Editar Quiz',
                        color=ft.Colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=ft.Icons.QUIZ_ROUNDED, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        )
        )]))
    page.add(ft.Container(
        bgcolor=ft.Colors.with_opacity(0.4,ft.Colors.WHITE),
        padding=ft.padding.all(10),
        border_radius=ft.BorderRadius(top_left=10, top_right=10, bottom_right=10, bottom_left=10),
        width=page.width,
        content=ft.Column(controls=[
            ft.Row(width=page.width,controls=[ft.Text("Informações:", size=17, weight=ft.FontWeight.BOLD),ft.IconButton(icon=ft.Icons.ADD_ROUNDED,on_click=lambda _:adicionar_dialog(page))],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row(width=page.width,controls=[ft.Text(f'N° de perguntas e respostas: {len(perguntas_l)}', size=16)]),
            
        ])
    ))


    def container_pergunta(pergunta,resposta,n_linha):
        # Mostra uma pergunta na tela
        # sanitize strings outside of f-string expressions to avoid backslashes inside braces
        safe_pergunta = pergunta.replace("\n", " ")
        safe_resposta = resposta.replace("\n", " ")
        return ft.Card(color=ft.Colors.with_opacity(0.5,ft.Colors.WHITE),width=page.width,
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.ABC_ROUNDED,size=40,color=ft.Colors.BLUE_900),
                        title=ft.Text(f"Pergunta N°: {n_linha+1}",weight=ft.FontWeight.W_900),
                    ),
                    ft.Text(value=f'Pergunta: {safe_pergunta}'),
                    ft.Text(value=f'Resposta: {safe_resposta}'),
                    ft.Row(
                        [ft.ElevatedButton(text='Excluir Pergunta',icon=ft.Icons.DELETE_ROUNDED,on_click=lambda e, i=n_linha: excluir_pergunta(i),icon_color=ft.Colors.RED,bgcolor=ft.Colors.TRANSPARENT)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
    for n_linha in range(len(perguntas_l)):
        page.add(container_pergunta(perguntas_l[n_linha],respostas_l[n_linha],n_linha))


    page.update()
    
    
def main(page: ft.Page):
# Função principal do app
    page.scrollable = ft.ScrollMode.HIDDEN
    page.clean()
    page.title = "Quiz 6X2"
    page.bgcolor = ft.Colors.LIGHT_BLUE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    
    def iniciar_quiz():
        # Começa o quiz
        
        # Elementos do Dialog
        quantidade_perguntas = ft.TextField(label='Quantidade de perguntas:',value=10)
        permissao_voz = ft.Checkbox(label="Ler perguntas em voz alta", value=True)
        
        
        
        def fechar_dlg(e=None):
            # Fecha a janela
            dlg.open = False
            page.update()
        def abrir_page_quiz(e=None):
            # Abre a página do quiz
            if quantidade_perguntas.value and 1 <= int(quantidade_perguntas.value) <= len(perguntas_l):
                num_perguntas = int(quantidade_perguntas.value)
                dlg.open = False
                page.open(ft.SnackBar(content=ft.Text(f'Iniciando quiz com {num_perguntas} perguntas...'),bgcolor=ft.Colors.GREEN))
                fechar_dlg()
                perguntas(page, num_perguntas,permissao_voz.value)
                page.update()
            else:
                page.open(ft.SnackBar(content=ft.Text(f'Insira um número válido entre 1 e {len(perguntas_l)}!'),bgcolor=ft.Colors.RED))
                page.update()
                
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text('Escolha a quantidade de perguntas.', weight=ft.FontWeight.BOLD, size=20),
            content=ft.Column(
                controls=[
                    quantidade_perguntas,
                    permissao_voz,
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Image(width=300,height=300,src='https://i.pinimg.com/736x/12/d3/fd/12d3fd7fb251029749a0ae762159f21b.jpg',expand=True,border_radius=ft.border_radius.all(10))])
                    
                ]
            ),
            actions=[
                ft.TextButton("Ok", on_click=abrir_page_quiz),
                ft.TextButton("Cancelar", on_click=fechar_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.open(dlg)
        page.update()
        
        
    page.add(
        ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=10, right=10,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.QUIZ_ROUNDED, color=ft.Colors.WHITE,size=30),
                    ft.Text(
                        value='Quiz 6X2',
                        color=ft.Colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=ft.Icons.QUIZ_ROUNDED, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        ),
    ),
                               ])
    )
    def botoes_g(texto,icon,funcao):
        # Cria um botão grande
        return ft.ElevatedButton(
        on_click=funcao,
        width=250, height=250,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Icon(name=icon, size=100),
                ]),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Text(texto, size=12, text_align=ft.TextAlign.CENTER)
                ]),
        ])
        )
    page.add(
        ft.Column(scroll=ft.ScrollMode.HIDDEN, alignment=ft.MainAxisAlignment.START, width=page.width, controls=[
            ft.Container(expand=True, margin=15, content=ft.Column(controls=[
                ft.Text("\n", size=27),
                ft.GridView(
                    expand=True,
                    runs_count=7,
                    max_extent=250,
                    child_aspect_ratio=1,
                    spacing=20,
                    run_spacing=20,
                    controls=[
        botoes_g('Iniciar Quiz.', ft.Icons.PLAY_ARROW_ROUNDED, lambda e: iniciar_quiz()),
        botoes_g('Editar Questões', ft.Icons.EDIT_ROUNDED, lambda e: editar_perguntas(page))
    ]
                )
            ]))
        ])
    )
    
ft.app(target=main)