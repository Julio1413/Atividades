import flet as ft
import os
import random
import time
import playsound3

with open('perguntas.txt','r', encoding="utf-8") as file:
    perguntas_l = file.readlines()
with open('respostas.txt','r', encoding="utf-8") as file:
    respostas_l = file.readlines()
def editar_perguntas(page):
    page.clean()
    page.update()
    page.scroll = ft.ScrollMode.AUTO
    page.add(
        ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=10, right=10,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.QUIZ_ROUNDED, color=ft.Colors.WHITE,size=30),
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
            ft.Text("Informações:", size=17, weight=ft.FontWeight.BOLD),
            ft.Text(f'N° de perguntas e respostas: {len(perguntas_l)}', size=16),
        ])
    ))
    def container_pergunta(pergunta,resposta):
        return
    for n_linha in range(len(perguntas_l)):
        pass
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
    ft.Text(f'\n',size=1),
                               ]))
    page.update()
    
def main(page: ft.Page):
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