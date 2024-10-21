from modules.list_editor import list_editor
import time


class App(list_editor):
    def start_app(self):
        print("Базові перетворення списків")
        data=list(input("Введіть елементи для списку ось так (1, 2, 3, 4) ").split(','))
        self.create_data(data)
        self.save_history()
        self.list_command()


    def list_command(self):
        if len(self.data)==0:
            self.start_app()
        time.sleep(1)
        print("\n\n\nМеню вибору\n0.Вивести список чисел\n1.Створити список:\n2.Додати елемент(и)\n3.Видалити елемент(и)\n4.Список + Список \n5.Сортування елементів \n6.Очистити список\n7.Історія сесії\n8.Видалити сесію\n9.Повернутися до списку\n10.Перевернути список\n11.Закінчити роботу")
        answer=input("Введіть номер операції: ")
        if answer=='0':
            self.show_list()
            time.sleep(2)
            self.history.append(self.data)
            self.list_command()
        elif answer=='1':
            self.start_app()
        elif answer=='2':
            self.add_menu()
            self.save_history()
        elif answer=='3':
            self.delete_menu()
            self.save_history()
        elif answer=='4':
            self.concate_menu()
            self.save_history()
        elif answer=='5':
            swap=str(input("Введіть чи True - якщо порядок спадання \nВведіть False порядок зростання: "))
            if swap=="True":
                swap=True
            else:
                swap=False
            self.sort_list(reverse=swap)
            self.save_history()
            self.list_command()
        elif answer=='6':
            self.clear_list()
            self.save_history()
            self.list_command()
        elif answer=='7':
            self.history_list()
            self.save_history()
            self.list_command()
        elif answer=='8':
            self.delete_history_list()
            self.list_command()
        elif answer=='9':
            self.retutn_list()
            self.save_history()
            self.list_command()
        elif answer=='10':
            self.data=self.data[::-1]
            self.save_history()
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
    def save_history(self):
        self.history.append(self.data)
        self.write_history()

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
        print("Пока")
    def concate_menu(self):
        my_input=list(input("Введіть масив який хочете добавити").split(','))
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
if __name__ == '__main__':
    app=App()
    app.list_command()
    print("Ну все кінець")