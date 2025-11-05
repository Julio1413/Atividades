import flet as ft
import os
import random
import time
import playsound3

with open('perguntas.txt','r', encoding="utf-8") as f:
    perguntas_l = f.readlines()
with open('respostas.txt','r', encoding="utf-8") as f:
    respostas_l = f.readlines()
def editar_perguntas(page):
    def save_files():
        # salva as listas atuais nos arquivos para persistência
        with open('perguntas.txt', 'w', encoding='utf-8') as f:
            f.writelines(perguntas_l)
        with open('respostas.txt', 'w', encoding='utf-8') as f:
            f.writelines(respostas_l)

    def excluir_pergunta(n_linha):
        # remove a pergunta e resposta pelo índice, salva e recarrega a interface
        if 0 <= n_linha < len(perguntas_l):
            perguntas_l.pop(n_linha)
            respostas_l.pop(n_linha)
            save_files()
            editar_perguntas(page)
    page.clean()
    page.update()
    page.scroll = ft.ScrollMode.AUTO
    def adicionar_dialog(page):
        nova_pergunta = ft.TextField(label='Nova pergunta:',hint_text=random.choice(perguntas_l))
        nova_resposta = ft.TextField(label='Nova resposta:',hint_text=random.choice(respostas_l))

        def close_dlg(e=None):
            dlg.open = False
            page.update()

        def add_p(e=None):
            pergunta = nova_pergunta.value.strip()
            resposta = nova_resposta.value.strip()
            if pergunta and resposta:
                perguntas_l.append(f'{pergunta}\n')
                respostas_l.append(f'{resposta}\n')
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
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Image(width=300,height=300,src='https://i.pinimg.com/736x/12/d3/fd/12d3fd7fb251029749a0ae762159f21b.jpg',expand=True)])
                    
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
    page.add(
        ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=10, right=10,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS_ROUNDED, icon_color=ft.Colors.WHITE,icon_size=30,on_click=lambda _: main(page)),
                    ft.Text(
                        value='Editar Quiz.',
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
            ft.Row(expand=True,controls=[ft.Text("Informações:", size=17, weight=ft.FontWeight.BOLD),ft.IconButton(icon=ft.Icons.ADD_ROUNDED,on_click=lambda _:adicionar_dialog(page))],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row(expand=True,controls=[ft.Text(f'N° de perguntas e respostas: {len(perguntas_l)}', size=16)]),
            
        ])
    ))


    def container_pergunta(pergunta,resposta,n_linha):
        return ft.Card(color=ft.Colors.with_opacity(0.5,ft.Colors.WHITE),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.QUESTION_MARK_SHARP,size=22),
                        title=ft.Text(f"Pergunta N°: {n_linha+1}"),
                    ),
                    ft.Text(f'Pergunta: {pergunta.replace("\n","")}',weight=ft.FontWeight.BOLD),
                    ft.Text(f'Resposta: {resposta.replace("\n","")}'),
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
    
    
    
    
    
def perguntas(page):
    page.clean()
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
    ft.Text(f'\n',size=1)]))
    page.add(ft.Placeholder(
        expand=True, color=ft.Colors.random()))
    page.update()
    
def main(page: ft.Page):
    page.clean()
    page.title = "Quiz 6X2"
    page.bgcolor = ft.Colors.LIGHT_BLUE
    page.theme_mode = ft.ThemeMode.LIGHT
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
        botoes_g('Iniciar Quiz.', ft.Icons.PLAY_ARROW_ROUNDED, lambda e: perguntas(page)),
        botoes_g('Editar Questões', ft.Icons.EDIT_ROUNDED, lambda e: editar_perguntas(page))
    ]
                )
            ]))
        ])
    )
    
ft.app(target=main)