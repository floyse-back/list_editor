import os
import ast
import datetime
class list_editor():
    def Create_Time_List(self,data):
        new_list=[]
        for i in range(0,len(data)-1,2):
            new_list.append((data[i],ast.literal_eval(data[i+1])))
        return new_list


    def read_full_history(self):
        try:
            data=[]
            with open("history.txt",'r',encoding='utf-8') as file:
                for i in file.readlines():
                    data.append(i.replace('\n',''))
            return data
        except FileNotFoundError:
            print("Історія порожня")


    def write_history(self,content):
        try:
            with open('history.txt','a',encoding='utf-8') as file:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Time: {now}\n")
                file.write(f'{content}\n')
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


    def typed_list(self,data:list,reverse=True):
        float_and_int_list=[]
        string_list=[]
        for i in data:
            typed=i[0]
            index=i[1]
            try:
                ft=float(typed)
                try:
                    el_int=int(typed)
                    float_and_int_list.append((el_int,index))
                except:
                    float_and_int_list.append((ft,index))
            except:
                string_list.append(i)
        float_and_int_list.sort(reverse=reverse)
        string_list.sort(reverse=reverse)
        return float_and_int_list +string_list
