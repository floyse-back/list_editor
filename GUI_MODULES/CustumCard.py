import time
import threading
import flet as ft

from GUI_MODULES.ElevateList import ElevateButs
from GUI_MODULES.HistoryList import HistoryList


class CustomCard(ft.Card):
    def __init__(self,page:ft.Page,route):
        self.page=page
        self.last_event=None
        self.route=route

        #Ref
        self.dropdownRef=ft.Ref[ft.Dropdown]()
        self.SaveRef=ft.Ref[ft.ElevatedButton]()
        self.Card=ft.Ref[ft.Card]()
        self.field=ft.Ref[ft.TextField]()
        self.sizeRef=ft.Ref[ft.Text]()
        self.Add_but=ft.Ref[ft.ElevatedButton]()
        #Ref
        self.ListBut = ElevateButs(self.sizeRef, self.dropdownRef, self.page)
        super().__init__(
                ref=self.Card,
                width=500,
                margin=ft.margin.only(top=5,bottom=5),
                shadow_color=ft.colors.WHITE24,
                surface_tint_color=ft.colors.GREEN_500,
                show_border_on_foreground=True,
                )
        if self.route=="/":
            self.HomePage()
        elif self.route=="/history":
            self.History = HistoryList(page)
            self.history()
    def history(self):
        self.Card.current.content=ft.Column(
            scroll="auto",
            height=750,
            horizontal_alignment="center",
            controls=[
                ft.Row(
                    controls=[ft.Text(value="History",weight="bold",size=35)],
                    alignment="center"
                ),
                ft.Row(
                    controls=self.History.history_check(),
                    alignment="center"
                )
            ]
        )




    #To Homepage
    def Text_Upload(self,event):
        if self.last_event == "blur" and event.name == "click":
            pass
        else:
            # Блокуємо кнопку, щоб уникнути повторного натискання
            self.Add_but.current.disabled = True
            self.update_button_state()

            # Додаємо кнопку до списку
            self.ListBut.add_button(val=self.field.current.value)

            self.field.current.value = ''
            self.field.current.update()

            self.sizeRef.current.value = f"Розмір списку {self.ListBut.Listlength()}"
            self.sizeRef.current.update()

            self.lock_button_temporarily(self.Add_but.current)

        self.last_event = event.name
    def lock_button_temporarily(self, button, lock_duration=0.04):
        # Блокуємо кнопку
        button.disabled = True
        self.update_button_state()

        # Виконуємо розблокування через lock_duration секунд у фоновому потоці
        def unlock_button():
            time.sleep(lock_duration)
            button.disabled = False
            self.update_button_state()

        threading.Thread(target=unlock_button).start()
    def update_button_state(self):
        # Оновлюємо стан кнопки
        self.Add_but.current.update()
    def HomePage(self):
        def value_get(event):
            if "Перевернути список"==self.dropdownRef.current.value:
                self.ListBut.reverse_list()
            elif "Порядок зростання"==self.dropdownRef.current.value:
                self.ListBut.sorted_list(reverse=False)
            elif "Порядок спадання"==self.dropdownRef.current.value:
                self.ListBut.sorted_list(reverse=True)
            self.ListBut.dissabled_correct_icons()
        self.Card.current.content=ft.Column(
                    scroll="auto",
                    height=700,
                    horizontal_alignment='center',
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value="ListEditor",
                                    font_family="Roboto",
                                    size=40,
                                    weight="bold",
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value="      Список:",
                                    font_family="Roboto",
                                    size=25,
                                    weight="bold",
                                ),
                                ft.Icon(
                                    name=ft.icons.LIST,
                                    size=25,
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[
                                ft.TextField(
                                    ref=self.field,
                                    width="auto",
                                    bgcolor=ft.colors.WHITE24,
                                    border_color=ft.colors.WHITE54,
                                    on_blur=self.Text_Upload,
                                ),
                                ft.ElevatedButton(
                                    ref=self.Add_but,
                                    bgcolor=ft.colors.GREEN,
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.ADD,
                                                size=35,
                                            ),
                                            ft.Text(
                                                value="ADD",
                                                size=35,
                                                weight="bold",
                                                font_family="Roboto"
                                            ),
                                        ],
                                        alignment="center",
                                    ),
                                    width="auto",
                                    height="auto",
                                    on_click=self.Text_Upload
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    ref=self.SaveRef,
                                    on_click=self.ListBut.saveStorage,
                                    bgcolor=ft.colors.GREEN,
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.SAVE,
                                                size=35,
                                            ),
                                            ft.Text(
                                                value="Save",
                                                size=35,
                                                weight="bold",
                                                font_family="Roboto"
                                            ),
                                        ],
                                        alignment="center",
                                    ),
                                    width="auto",
                                    height="auto",
                                ),
                                ft.ElevatedButton(
                                    on_click=self.ListBut.clear_list,
                                    bgcolor=ft.colors.RED,
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.CLEAR_ALL,
                                                size=35,
                                            ),
                                            ft.Text(
                                                value="Clear",
                                                size=35,
                                                weight="bold",
                                                font_family="Roboto"
                                            ),
                                        ],
                                        alignment="center",
                                    ),
                                    width="auto",
                                    height="auto",
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[ft.Dropdown(
                                    ref=self.dropdownRef,
                                    options=[
                                        ft.dropdown.Option("Cвій порядок"),
                                        ft.dropdown.Option("Порядок спадання"),
                                        ft.dropdown.Option("Порядок зростання"),
                                        ft.dropdown.Option("Перевернути список"),                                    ],
                                    bgcolor=ft.colors.WHITE24,
                                    on_change=value_get,
                                )],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    ref=self.sizeRef,
                                    value=f"Розмір списку {self.ListBut.Listlength()}",
                                    size=35,
                                    weight="bold",
                                    font_family="Roboto"
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            controls=[
                                self.ListBut,
                            ],
                            alignment="center",

                        ),
                    ]
                )


