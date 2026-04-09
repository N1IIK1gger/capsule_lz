import os
import datetime
import pandas as pd


def logging(func):#создание логгера
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        user=os.getlogin()#юзер
        func_name = func.__name__#название функции
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        time = datetime.datetime.now().strftime("%H:%M:%S")

        if os.path.exists("logs.csv"):#Проверяем существует ли такой файл
            file = pd.read_csv('logs.csv')#Существует-читаем
            id = len(file)#Количество строк в файле, чтобы определить следующий id
            new_row = pd.DataFrame({'id': [id],'pc_username': [user],'function_name': [func_name],'Date in date.month.year': [date],'Time': [time]})
            new_row.to_csv('logs.csv', mode='a', header=False, index=False)

        else:
            df = pd.DataFrame({'id': [0],'pc_username': [user],'function_name': [func_name], 'Date in date.month.year': [date],'Time': [time]})
            df.to_csv('logs.csv', index=False)   #Сохраняем

        return res
    
    return wrapper
