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

    
    mensaje = ft.Text(
        "Hola Mundo",
        size = 18,
        color = "blue"
        text_align = ft.FontWeight.Center
    )


    def cambiar_texto(e):
        mensaje.value = "El mensaje cambio"
        mensaje.color = "purple"
        page.update()

    boton1 = ft.button(
        "cambiar mensaje",
        on_click = cambiar_texto,
        icon = ft.icons.CHANGE_CIRCULE
    )

    tarjeta = ft.Container(
        content = ft.column(
            controls = [
                mensaje,
                boton1
            ]
            aliment = ft:MainAxisAligment.CENTER,
            horizontal_Aligment = ft.CrossAxisAligment.CENTER
            spacing = 20
        ),
        wdith = 250,
        heigth = 200,
        padding = 20,
        border_radius = 15
        bgcolor = ft.Colors:GREY_300
        shadow = ft:BoxShadow(
            blur_radius = 10,
            spread_radius = 1
            color = ft..Color.Black26
        )
    )

    page.add()
        
    ft.app(target = main)