import time

import flet as ft
from modules.list_editor import list_editor

class ElevateButs(ft.Column):
    def __init__(self,sizeRef:ft.Ref[ft.Text](),dropdownRef:ft.Ref[ft.Dropdown](),page:ft.Page):
        super().__init__()
        #
        self.last_value_textfield=[]
        self.controls=[]
        self.dropdownRef = dropdownRef
        self.page = page
        self.sizeRef=sizeRef
        self.value_text_fields=[]
        self.length=self.Listlength()
        self.up_disabled=False
        self.down_disabled=False
        #
        self.content=self.page.client_storage.get("saveContent")
        #Імпорт list_editor
        self.list_editor=list_editor()
        if self.content:
            self.create_Buttons(self.content)

    def create_Buttons(self,content:list):
        if not content:
            return
        self.controls.clear()
        for i in content:
            self.add_button(val=i,up=False)
        if self.controls:
            self.page.update()




    def add_button(self,val="",up=True):
        if up:
            val=self.check_once(val)
        key_up=f"up_{len(self.controls)}"
        key_down=f"down_{len(self.controls)}"
        text_field = ft.TextField(
            value=val,
            bgcolor=ft.colors.WHITE24,
            border_color=ft.colors.WHITE54,
            color=ft.colors.WHITE,
            border_width=2,
            border_radius=10,
            label="ADD",
            width="auto",
            text_size=25,
            on_blur=lambda e: self.get_list()
        )
        new_row = ft.Row(
            controls=[
                text_field,
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    bgcolor=ft.colors.RED,
                    icon_size=25,
                    on_click=lambda e: self.delete_row(new_row),
                ),
                ft.Column(
                    controls=[ft.IconButton(
                        icon=ft.icons.ARROW_UPWARD,
                        bgcolor=ft.colors.TRANSPARENT,
                        icon_size=25,
                        key=key_up,
                        on_click=lambda e,my_key=key_up:self.Up_Go(e,my_key),

                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_DOWNWARD,
                        bgcolor=ft.colors.TRANSPARENT,
                        on_click=lambda e,my_key=key_down:self.Down_Go(e,my_key),
                        icon_size=25,
                        key=key_down,
                    )],
                )
            ]
        )
        self.controls.append(new_row)
        if up==True:
            self.dissabled_correct_icons()
            if self.controls:
                self.update()



    def delete_row(self, row):
        self.controls.remove(row)
        self.sizeRef.current.value=f"Розмір списку {self.Listlength()}"
        self.sizeRef.current.update()
        self.dissabled_correct_icons()
        self.update()


    def change_value_textfield(self,data:list):
        for i in data:
            ind = i[1]
            text = i[0]
            self.controls[ind].controls[0].value=text
        self.update()

    def check_once(self,element):
        try:
            new_eval=eval(element)
            if new_eval==element:
                return element
            else:
                return new_eval
        except:
            return element
    def get_list(self):
        def check_all(data:list):
            answer=[]
            new_list=[]

            for v,i in enumerate(data):
                try:
                    swap=eval(i)
                    new_list.append((swap,v))
                except:
                    pass
            for i in new_list:
                ind=i[1]
                text=i[0]
                if str(data[ind])!=str(text):
                    answer.append((text,ind))
            self.change_value_textfield(answer)
        self.value_text_fields=[]
        for controls in self.controls:
            temp=controls.controls[0].value
            self.value_text_fields.append(temp)
        if self.value_text_fields:
            check_all(self.value_text_fields)
    def Listlength(self):
        return len(self.controls)




    #Для редагування змін стрілок
    def dissabled_correct_icons(self):
        for i,controls in enumerate(self.controls):
            up=(i==0)
            down=(i==len(self.controls)-1)
            self.controls[i].controls[2].controls[0].disabled = up
            self.controls[i].controls[2].controls[1].disabled = down
        if self.controls:  # Переконайтеся, що контролі існують
            self.update()





    def save_list(self):
        value=[]
        for control in self.controls:
            value.append(control.controls[0].value)

    def Up_Go(self,event,key):
        def find_control():
            for i, controls in enumerate(self.controls):
                if controls.controls[2].controls[0].key == key:
                    return i
        ind=find_control()
        temp=self.controls[ind]
        self.controls[ind]=self.controls[ind-1]
        self.controls[ind-1]=temp
        self.update()
        self.dissabled_correct_icons()
    def Down_Go(self,event,key):
        def find_control():
            for i, controls in enumerate(self.controls):
                if controls.controls[2].controls[1].key == key:
                    return i
        ind=find_control()
        temp=self.controls[ind]
        self.controls[ind]=self.controls[ind+1]
        self.controls[ind+1]=temp
        self.update()
        self.dissabled_correct_icons()



    def clear_list(self, event):
        # Очищення списку, створюючи новий порожній список
        self.controls = []  # Призначаємо новий порожній список
        self.sizeRef.current.value = f"Розмір списку {self.Listlength()}"
        self.sizeRef.current.update()
        self.update()

    def saveStorage(self,event=''):
        new_data=[]
        for controls in self.controls:
            new_data.append(controls.controls[0].value)
        self.page.client_storage.set("saveContent",new_data)
        self.list_editor.write_history(new_data)

    def reverse_list(self):
        self.controls=self.controls[::-1]
        self.update()
        self.saveStorage()

    def sorted_list(self, reverse=False):
        indexed_values = [(ctrl.controls[0].value, i) for i, ctrl in enumerate(self.controls)]
        indexed_values=self.list_editor.typed_list(indexed_values,reverse=reverse)
        sorted_controls = [self.controls[i] for _, i in indexed_values]
        self.controls = sorted_controls
        self.update()
