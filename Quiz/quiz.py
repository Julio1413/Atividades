import flet as ft
import os
import random
import time
import playsound3

with open('perguntas.txt','r') as file:
    perguntas = file.readlines()
with open('respostas.txt','r') as file:
    respostas = file.readlines()
print (perguntas)
print (respostas)

def resultados(acertos):
    pass
def main(page: ft.Page):
    def verificar_resposta():
        pass
    def acertou():
        pass
    def errou():
        pass
    def proxima_pergunta(e):
        pass
    acertos=0
    page.title = "Quiz 6X2"
    page.bgcolor = ft.Colors.LIGHT_BLUE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    
    
    #Construção da página
    
    
ft.app(target=main)
