import flet as ft
import os
import platform
import pages


def pasta_global():
    sistema = platform.system()
    if sistema == "Windows": pasta_global = r'C:\CubePy\6X2'
    elif "ANDROID_BOOTLOGO" in os.environ or (sistema == "Linux" and "arm" in platform.uname().machine): pasta_global = os.getenv("FLET_APP_STORAGE_DATA")  # Pasta de dados do app no Android
    elif sistema == "Linux": pasta_global = os.path.expanduser("~/Cubepy/6X2")  # Diretório oculto no home do usuário
    else: pasta_global = r'C:\CubePy\6X2'  # Valor padrão caso o sistema não seja identificado
    os.makedirs(pasta_global, exist_ok=True)
    return str(pasta_global)


def header( 
            titulo,
            icone,
            page,
            destino,
            icone_btn=ft.Icons.ARROW_BACK_IOS_ROUNDED,
           ):
    return ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=10, right=10,bottom=10),
            blur=(10,10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon_color=ft.Colors.WHITE,
                        icon=icone_btn,
                        on_click=lambda _:destino(page),
                        icon_size=25,
                    ),
                    ft.Text(
                        value=titulo,
                        color=ft.Colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(name=icone, color=ft.Colors.WHITE,size=30),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            height=50,
        ),
    ),
    ft.Text(f'\n',size=1)
                               ])