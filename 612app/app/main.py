import flet as ft
import pages
def home (page: ft.Page):
    page.title = "6X2"
    page.scroll = "auto"
    page.window_width = 900
    page.window_height = 600
    page.bgcolor = ft.Colors.DEEP_PURPLE
    page.theme_mode = ft.ThemeMode.DARK
    
    pages.home(page)
    page.update()
ft.app(target=home)