import flet
import flet as ft
from  GUI_MODULES.Header import Header
from GUI_MODULES.CustumCard import CustomCard
def main(page:ft.Page):
    page.title="List Corrector"
    page.horizontal_alignment="center"
    page.scroll="auto"
    def change_route(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    appbar=Header(page, "Hello"),
                    controls=[
                        CustomCard(page,"/")
                    ]
                )
            )
        if page.route =="/go":
            page.go("/history")
        if page.route == "/history":
            page.views.append(
                ft.View(
                    route="/history",
                    appbar=Header(page, "History"),
                    controls=[
                        CustomCard(page,"/history")
                    ]
                    
                )
            )
        page.update()
    page.on_route_change=change_route
    page.go(page.route)
flet.app(target=main,view=ft.WEB_BROWSER)