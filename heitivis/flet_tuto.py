#Importando
import flet as ft


# tela
def main(page:ft.Page):
    page.add(
        ft.Text(value='Flet, tela', weight=ft.FontWeight.BOLD)
    )

    texto = ft.TextField(label='Entrada')
    page.add(texto)
    page.add(
        ft.TextButton(content='Printar texto',on_click=lambda _:print(texto.value))
    )
    page.add(ft.Icon(icon=ft.Icons.ABC))
    print(texto.value)

ft.app(main)

