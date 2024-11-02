import flet as ft




def Header(page:ft.Page,title):
    selected_list={
        "/":{
            "disabled":False,
            "selected":False,
            "route":lambda e:page.go("/"),
            "icons":ft.icons.HOME,
        },
        "/history": {
            "disabled": False,
            "selected":False,
            "route": lambda e: page.go("/history"),
            "icons": ft.icons.HISTORY,
        }
    }
    app=ft.AppBar(bgcolor=ft.colors.WHITE24, title=ft.Text(value=f"{title}")
    )
    for i in list(selected_list.keys()):
        app.actions.append(
            ft.IconButton(icon=selected_list[i]["icons"],
                          on_click=selected_list[i]["route"],
                          padding=10,
                          icon_size=30,
                          selected=selected_list[i]["selected"],
                          ),
        )
    app.actions.append(
        ft.IconButton(icon=ft.icons.EXIT_TO_APP,
                      on_click=lambda e: page.window_close(),
                      padding=10,
                      icon_size=30,
                      ),
    )
    return app
