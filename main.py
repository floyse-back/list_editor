from modules.list_editor import list_editor
import time
import keyboard


class App(list_editor):
    def start_app(self):
        print("Базові перетворення списків")
        data=list(input("Введіть елементи для списку ось так (1, 2, 3, 4) ").split(','))
        self.create_data(data)
        self.save_history(value="Створити список")
        self.list_command()


    def list_command(self):
        if len(self.data)==0:
            self.start_app()
        time.sleep(1)
        print("\n\n\nМеню вибору\n0.Вивести список чисел\n1.Створити список:\n2.Додати елемент(и)\n3.Видалити елемент(и)\n4.Список + Список \n5.Сортування елементів \n6.Очистити список\n7.Історія сесії\n8.Видалити сесію\n9.Повернутися до списку\n10.Перевернути список\n11.Закінчити роботу")
        answer=input("Введіть номер операції: ")
        data=self.data
        if answer=='0':
            self.show_list()
            self.check_enter()
            self.list_command()
        elif answer=='1':
            self.start_app()
        elif answer=='2':
            self.add_menu()
            self.save_history(value='Додати елемент')
        elif answer=='3':
            self.delete_menu()
            self.save_history(value="Видалити елемент")
        elif answer=='4':
            self.concate_menu()
            self.save_history(value="Список + Список")
        elif answer=='5':
            swap=str(input("Введіть чи True - якщо порядок спадання \nВведіть False порядок зростання: "))
            if swap=="True":
                swap=True
            else:
                swap=False
            self.sort_list(reverse=swap)
            self.save_history(value="Сортування елементів")
            self.list_command()
        elif answer=='6':
            self.clear_list()
            self.save_history(value='Очистити список')
            self.list_command()
        elif answer=='7':
            self.read_full_history()
            self.check_enter()
            self.list_command()
        elif answer=='8':
            self.delete_history_list()
            self.list_command()
        elif answer=='9':
            data=self.data
            self.retutn_list()
            if data!=self.data:
                self.save_history(value=f'Повернутися від списку {data} до списку {self.data}')
            self.list_command()
        elif answer=='10':
            self.data=self.data[::-1]
            self.save_history(value='Перевернути список')
            self.list_command()
        elif answer=='11':
            self.close_list()
        else:
            print("Ви ввели щось не то")
            self.list_command()
    def add_menu(self):
        element=input("Введіть елемент: ")

        for i, value in enumerate(self.data):
            print(f"{i}.{value}")
        position=input("Введіть позицію або(None): ")
        if position!="None":
            try:position=int(position)
            except:
                print("Введіть або None або число... для (Позиції)")
                self.add_element()
            swap=input("Введіть чи потрібно заміняти елемент True/False: ")
            if swap=='True':
                swap=True
            else:
                swap=False
            self.add_element(element,position,swap)
        else: self.add_element(element)
        self.list_command()
        self.show_list()
    def save_history(self,value):
        self.history.append(self.data)
        self.write_history(value=f"{value}")

    def delete_menu(self):
        try:
            if len(self.data)!=0:
                for i,value in enumerate(self.data):
                    print(f"{i}.{value}")
                val=input("Введіть позицію")
                while int(val)>=len(self.data):
                    print(f"Введіть число від 0 до {len(self.data)-1}")
                    val=int(input("Введіть позицію"))
                self.delete_element(int(val))
            else:
                print("Створіть список для початку")
                self.start_app()
        except TypeError:
            print("Введіть елемент без ком і так далі!!!")
            self.delete_menu()
        finally:
            self.list_command()
    def close_list(self):
        print("Пока")
        exit(404)
    def concate_menu(self,elem=0):
        while True:
            try:
                if elem==0:
                    my_txt=int(input("1.Добавити масив з історії\n2.Ввести масив\nОберіть операцію: "))
                else:
                    my_txt=2
                if my_txt==1:
                    while True:
                        try:
                            if len(self.history)==0:
                                print("Вибачте але історія порожня")
                                self.concate_menu(elem=1)
                                return 0
                            else:
                                try:
                                    while True:
                                        self.history_list()
                                        my_txt=int(input("Виберіть що потрібно добавити до списку: "))
                                        if my_txt<len(self.history) and my_txt>0:
                                            for i in self.history[my_txt]:
                                                self.data.append(i)
                                            return 0
                                except:pass

                        except Exception as ex:
                            print(ex)



                if my_txt==2:
                    my_input = list(input("Введіть масив який хочете добавити").split(','))
                    break
            except Exception as ex:
                print(ex)
        self.concate_list(my_input)
        self.list_command()
    def history_list(self):
        for i,key in enumerate(self.history):
            print(f"{i}.{key}")
    def delete_history_list(self):
        self.history=[]
        self.delete_history()
    def retutn_list(self):
        if len(self.history)==0:
            return -1
        self.history_list()
        while True:
            try:
                n=int(input("Введіть число для повернення до списку"))
                if len(self.history)-1>=n:
                    self.data=self.history[n]
                    break
                if len(self.history)==0:
                    break
            except:
                pass
    def check_enter(self):
        print("Якщо ви закінчили нажміть на Enter")
        keyboard.wait("enter")
if __name__ == '__main__':
    app=App()
    app.list_command()
    print("Ну все кінець")