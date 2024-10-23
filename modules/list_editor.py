import os
import ast


class list_editor():
    def __init__(self):
        self.data=[]
        self.history=self.read_history()
    """Створення списку"""
    def create_data(self,data:list=[1,2,3]):
        self.data=data
        self.show_list()
    def read_full_history(self):
        try:
            with open("history.txt",'r',encoding='utf-8') as file:
                for i in file.readlines():
                    print(i.replace('\n',''))
        except FileNotFoundError:
            print("Історія порожня")
    def write_history(self,value):
        try:
            with open('history.txt','a',encoding='utf-8') as file:
                if len(self.history)>0:
                    file.write(f'{value}\n')
                    file.write(f'{self.history[-1]}\n')
        except Exception as ex:print(f"{ex}- Error Write History")
    def delete_history(self):
        try:
            os.remove('history.txt')
        except:print("Error don`t delete history")
    def read_history(self):
        newlist=[]
        try:
            with open('history.txt','r',encoding='utf-8') as file:
                for i in file.readlines():
                    if str(i)[0]=='[':
                        txt = ast.literal_eval(i)
                        newlist.append(txt)
            return newlist
        except Exception as ex:
            #print(f"Error Read_history\n {ex} ")
            return []

    """Додавання елементу до списку"""
    def add_element(self,element,position=None,swap=False):
        if position is None or position =="None":
            self.data.append(element)
            return f"Успішно добавлено елемент в кінець поточного списку {element} в список"
        if swap:
            self.data[position]=element
        else:
            newdata=[]
            for i in range(0,len(self.data)):
                if i==position:
                    newdata.append(element)
                newdata.append(self.data[i])
            self.data=newdata
    """Видалення елементу за позицією"""
    def delete_element(self,position:int):
        self.data.pop(position)
        self.show_list()
    def concate_list(self,list_add):
        for i in list_add:
            self.data.append(i)
        self.show_list()

    def sort_list(self,**kwargs):
        intdata=[]
        try:
            intdata=list(map(int,self.data))
        except:"Не судьба"
        if intdata!=[]:
            intdata.sort(**kwargs)
            self.data=list(map(str,intdata))
        else:
            self.data.sort(**kwargs)
        self.show_list()

    def show_list(self):
        print(self.data)

    def clear_list(self):
        self.data=[]


