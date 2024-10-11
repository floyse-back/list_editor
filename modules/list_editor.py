





class list_editor():
    def __init__(self):
        self.data=[]
    """Створення списку"""
    def create_data(self,data:list=[1,2,3]):
        self.data=data
        self.show_list()

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