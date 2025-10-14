import flet as ft
import os
import random
import time
import playsound3

with open('perguntas.txt','r') as file:
    perguntas = file.readlines().lower()
with open('respostas.txt','r') as file:
    respostas = file.readlines().lower()
print (perguntas)
print (respostas)

def resultados(acertos):
    pass
def main(page: ft.Page):
    def acertou():
        pass
    def errou():
        pass
    def proxima_pergunta(e):
        pass
    acertos=0
    page.title = "Quiz 6X2"
    page.window_width = 400
    page.window_height = 600
    page.bgcolor = ft.Colors.LIGHT_BLUE
    page.update()
ft.app(target=main)
