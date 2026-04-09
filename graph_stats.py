import pandas as pd
import matplotlib.pyplot as plt
import getpass
from log import logging
import os

class Cost:

    def __init__(self):
        pass
    
    @logging # Добавили декоратор
    def processing(self):
        
        # Обработка файла
        data = pd.read_csv('log.csv')
        print("Прочитанные данные:")
        print(data.head())

        # Построение гистограммы

        x = data['Date'].tolist()
        y = data['Open'].tolist()
        y1 = data['High'].tolist()
        y2 = data['Close'].tolist()
        y3 = data['Low'].tolist()
        plt.scatter(x,y1, color = 'green')
        plt.bar(x,y)
        plt.bar(x,y2)
        plt.scatter(x,y3, color = 'red')
        plt.xlabel('Дата')
        plt.ylabel('Изменения')
        plt.title('Гистограмма стоимости акций Apple')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
        
# Определили функцию в main

def main():
    apple_cost = Cost()
    apple_cost.processing()

if __name__=="__main__":
    main()
