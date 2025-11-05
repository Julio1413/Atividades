from flet import Page, Text, Stack, Colors, ThemeMode, Icons, Column, MainAxisAlignment, ElevatedButton, ButtonStyle, RoundedRectangleBorder, GridView, ScrollMode, Container, Row, Icon, TextAlign, Brightness
import os
from pages import configs, hipoe, graficos, relatorio, glicapp, info_nutri, ferramentas


def inicial (page):
    page.clean()
    page.route = "/"
    pasta_global = ferramentas.pasta_global()
    page.floating_action_button = None
    if os.path.exists(os.path.join(pasta_global, "bright_mode.txt")):
        with open(os.path.join(pasta_global, "bright_mode.txt"), "r") as file:
            bright_mode = file.read().strip()
    else:
        with open(os.path.join(pasta_global, "bright_mode.txt"), "w") as file:
            file.write("0")
        bright_mode = "0"

    if bright_mode == "0":
        page.theme_mode = ThemeMode.SYSTEM
        if page.platform_brightness == Brightness.LIGHT:
            icon_color = Colors.BLACK
        else:
            icon_color = Colors.WHITE
    elif bright_mode == "1":
        page.theme_mode = ThemeMode.DARK
        icon_color = Colors.WHITE
    elif bright_mode == "2":
        page.theme_mode = ThemeMode.LIGHT
        icon_color = Colors.BLACK

    page.update()
    
    def botoes_g(texto,icon,funcao):
        return ElevatedButton(
        on_click=funcao,
        width=250, height=250,
        style=ButtonStyle(shape=RoundedRectangleBorder(radius=20)),
        content=Column(alignment=MainAxisAlignment.CENTER, controls=[
            Row(alignment=MainAxisAlignment.CENTER, controls=[
                Icon(name=icon, size=100, color=icon_color),
                ]),
            Row(alignment=MainAxisAlignment.CENTER, controls=[
                Text(texto, size=12, text_align=TextAlign.CENTER)
                ]),
        ])
        )
    
    menu = [
        botoes_g("Controle do diabetes",Icons.MEDICAL_INFORMATION_ROUNDED,lambda _:glicapp.glicapp(page)),
        botoes_g('Histórico de extremos',Icons.LOCAL_FIRE_DEPARTMENT,lambda _:hipoe.hipoe(page)),
        botoes_g('Gráficos de glicemia',Icons.INSIGHTS,lambda _:graficos.graficos(page)),
        botoes_g('Relatório de glicemia',Icons.DESCRIPTION_ROUNDED,lambda _:relatorio.relatorio(page)),
        botoes_g('Buscar alimentos',Icons.EMOJI_FOOD_BEVERAGE_ROUNDED,lambda _:info_nutri.info_nutri(page)),
    ]
    page.add(Stack([
        Column(scroll=ScrollMode.HIDDEN, alignment=MainAxisAlignment.START, width=page.width, controls=[
            Container(expand=True, margin=15, content=Column(controls=[
                Text("\n", size=27),
                GridView(
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
        ferramentas.header(titulo="Glicapp", icone=Icons.HOME_ROUNDED, page=page, destino=configs.configs,icone_btn=Icons.SETTINGS_ROUNDED)

    ], expand=True))

