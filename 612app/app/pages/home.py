import flet as ft
import pages
def home (page):
    
    

    def botoes_g(texto,icon,funcao, icon_color=ft.Colors.WHITE):
        return ft.ElevatedButton(
        on_click=funcao,
        width=250, height=250,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Icon(name=icon, size=100, color=icon_color),
                ]),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
                ft.Text(texto, size=12, text_align=ft.TextAlign.CENTER)
                ]),
        ])
        )
        
    menu = [
        botoes_g("Controle do diabetes",ft.Icons.MEDICAL_INFORMATION_ROUNDED,lambda _:None),
        
    ]
    page.add(ft.Stack([
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
                    controls=menu
                )
            ]))
        ]),
        pages.ferramentas.header(
            titulo="6X2", icone=ft.Icons.HOME, page=page, destino=None, icone_btn=ft.Icons.SETTINGS_ROUNDED
        )

    ], expand=True))
    page.update()
ft.app(target=home)