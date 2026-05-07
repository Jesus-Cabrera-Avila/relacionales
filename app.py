import flet as ft

def main(page: ft.Page):
    page.titlr = "m primer app de flet"

    page.bgcolor = "#00103d"

    page.add(
        ft.Text(
            "hola, Mundo",
            color = "#000000",
            size = 30,
            weight = ft.FontWeight.BOLD
        )
    )

    ft.app(target = main)