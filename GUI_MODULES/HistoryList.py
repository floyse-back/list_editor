import flet as ft
from anyio.abc import value
from flet_core.colors import TRANSPARENT

from modules.list_editor import list_editor

class HistoryList(ft.Column):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.list_editor = list_editor()
        self.page = page
        self.full_history = self.read_all_history()
    def history_check(self):
        if self.full_history:
            return self.build_history()
        else:
            return self.build_null_history()
    def read_all_history(self):
        return self.list_editor.read_full_history()
    def build_null_history(self):
        self.controls.append(
            ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.HOURGLASS_EMPTY,
                        size=100,
                    ),
                    ft.Text("Дуже чисто...",size=30,weight="bold"),
                ],
                alignment="center",
            )
        )
        return self.controls

    def clear_history(self,event):
        self.controls.clear()
        self.update()
        self.page.client_storage.clear()
        self.list_editor.delete_history()
        self.page.go("/go")

    def build_history(self):
        def on_clicked(event,history):
            self.page.client_storage.set("saveContent", history)
            self.page.snack_bar.open=True
            self.page.update()
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(color=ft.colors.WHITE,value="Copied",size=30,font_family="Roboto",weight="bold",text_align="center"),
            action="Alright",
            behavior=ft.SnackBarBehavior.FLOATING,
            bgcolor=ft.colors.GREEN,
            width=400,
            margin=90,
            duration=1500,
            elevation=6,
        )
        history_list=self.list_editor.Create_Time_List(self.full_history)
        NewColumn = ft.Column()
        for i in history_list:
            history_time=i[0]
            history_list=i[1]
            row1=ft.Row(
                controls=[
                    ft.Text(f"{history_time}", size=30, weight="bold"),
                ]
            )
            row2=ft.Row(
                controls=[
                    ft.TextField(
                        width=300,
                        value=f"{history_list}",
                        bgcolor=ft.colors.WHITE24,
                        disabled=True,
                        border_color=ft.colors.WHITE54,
                        multiline=True,
                    ),
                    ft.IconButton(
                        icon=ft.icons.COPY,
                        icon_size=30,
                        bgcolor=ft.colors.GREEN,
                        on_click=lambda e,history=history_list:on_clicked(e,history),
                    )
                ],
            )
            NewColumn.controls.append(
                row1
            )
            NewColumn.controls.append(row2)
        NewColumn.controls.append(
            ft.Row(
                controls=[
            ft.ElevatedButton(
                bgcolor=ft.colors.RED,
                color=ft.colors.WHITE,
                on_click=self.clear_history,
                content=ft.Row(
                    controls=[
                    ft.Icon(
                        name=ft.icons.CLEAR_ALL,
                    ),
                    ft.Text(value="Clear",weight="bold",size=40,font_family="Roboto",text_align="center",width=250),
                ],
                )
            )],
            alignment="center",
            )
        )
        self.controls.append(
            ft.Row(
                controls=[NewColumn]
            )
        )
        return self.controls