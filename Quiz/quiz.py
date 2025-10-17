import flet as ft
import os
import random
import time
import playsound3

with open('perguntas.txt','r', encoding="utf-8") as file:
    perguntas = file.readlines()
with open('respostas.txt','r', encoding="utf-8") as file:
    respostas = file.readlines()
    
def perguntas(page):
    page.clean()
    page.update()
    def resultados(acertos):
        pass
    def verificar_resposta():
        pass
    def acertou():
        pass
    def errou():
        pass
    def proxima_pergunta(e):
        pass
    acertos=0
    
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
    ft.Text(f'\n',size=1),
                               ])
    )
    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.all(10),
            content=ft.ElevatedButton(
                expand=True,
                on_click=lambda e: perguntas(page),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=20),
                    bgcolor=ft.colors.BLUE_600,
                    color=ft.colors.WHITE,
                    elevation=5,
                    overlay_color=ft.colors.BLUE_200,
                ),
                content=ft.Container(
                    margin=ft.margin.only(top=10, bottom=10),
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Text('Iniciar Quiz', size=20, weight=ft.FontWeight.BOLD),
                            ft.Text('10 perguntas aleatórias sobre Python', size=20, weight=ft.FontWeight.BOLD)
                        ]
                    )
                )
            )
        )
    )
        
    
ft.app(target=main)
