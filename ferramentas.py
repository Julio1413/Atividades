from pages import home
from flet import Text, SnackBar, Colors, TextField, KeyboardType, ElevatedButton, ButtonStyle, RoundedRectangleBorder, Icons
import platform, os
#padding geral da ui
def padding():
    return 17
import flet as ft
#cor para janela
def brightness(page):
    if page.theme_mode == ft.ThemeMode.LIGHT:
        container_color = ft.Colors.WHITE
    else:
        container_color = ft.Colors.BLACK87
    page.update()
    return container_color

#cor para texto
def brightness_text(page):
    if page.theme_mode == ft.ThemeMode.LIGHT:
        text_color = ft.Colors.BLACK87
    else:
        text_color = ft.Colors.WHITE
    page.update()
    return text_color

#pasta global
def pasta_global():
    sistema = platform.system()

    if sistema == "Windows":
        pasta_global = r'C:\CubePy\Glicapp'
        os.makedirs(pasta_global, exist_ok=True)
    elif "ANDROID_BOOTLOGO" in os.environ or (sistema == "Linux" and "arm" in platform.uname().machine):
        pasta_global = os.getenv("FLET_APP_STORAGE_DATA")  # Pasta de dados do app no Android
    elif sistema == "Linux":
        pasta_global = os.path.expanduser("~/Cubepy/glicapp")  # Diretório oculto no home do usuário
        os.makedirs(pasta_global, exist_ok=True)
    else:
        pasta_global = r'C:\CubePy\Glicapp'  # Valor padrão caso o sistema não seja identificado
        os.makedirs(pasta_global, exist_ok=True)
    return pasta_global

#ferramentas de interface (header e container)
def header( 
            titulo,
            icone,
            page,
            destino=home.inicial,
            icone_btn=ft.Icons.ARROW_BACK_IOS_ROUNDED,
           ):
    return ft.Column(controls=[ft.Container(height=90,
        content=ft.Container(alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=padding(), right=padding(),bottom=10),
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


def container(page,
              controles=[],
              ):
    return ft.Container(
            expand=True,
            margin=ft.margin.all(-10),
            padding=ft.padding.all(17),
            border_radius=ft.border_radius.only(top_left=42, top_right=42),
            bgcolor=brightness(page),
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=controles
            )
        )
def dialog(page,
    titulo,
    icone_d,
    icone_e,
    funcao_btn='',
    texto_btn='',
    conteudo=[]
):
    if funcao_btn and texto_btn: btn2 = ft.TextButton(texto_btn, on_click=funcao_btn)
    else: btn2=ft.Text('')
    
   
    dlg = ft.AlertDialog(
        bgcolor=ft.Colors.with_opacity(0.0, ft.Colors.WHITE),
        barrier_color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
        content=ft.Container(
            blur=(10, 10),
            bgcolor=ft.Colors.WHITE.with_opacity(0.2, ft.Colors.WHITE70),
            margin=ft.margin.only(top=6,left=4,right=4,bottom=4),
            border_radius=ft.border_radius.all(20),
            expand=True,
            height=450,
            width=400,
            padding=ft.padding.all(6),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # título
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Icon(name=icone_d),
                            ft.Text(titulo, size=17, weight=ft.FontWeight.BOLD),
                            ft.Icon(name=icone_e),
                        ]
                    ), 
                    ft.Divider(height=1),
                    ft.Column(width=400,
                        scroll=ft.ScrollMode.AUTO,
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        controls=[       
                            ft.Text('\n', size=3),
                            # conteúdo do dialog
                            ft.Column(controls=conteudo, alignment=ft.MainAxisAlignment.START),
                            ft.Text('\n', size=3),
                        ]
                    ),
                    ft.Divider(height=1),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton("Cancelar", on_click=lambda e: fechar_dialog(page, dlg)),
                            btn2
                        ]
                    )
                ]
            )
        )
    )


    return dlg

def fechar_dialog(page, dlg):
    dlg.open = False
    page.update()