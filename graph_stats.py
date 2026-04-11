import pandas as pd
import mplfinance as mpf
from main import func_lgn
@func_lgn
class Apple:
    
    def __init__(self, AAPL_csv):
        self.AAPL_csv = AAPL_csv
        self.data = None

    def dann(self):
        # берем данные из CSV файла
        self.data = pd.read_csv(self.AAPL_csv, parse_dates=True, index_col='Date')
        
        columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        if not all(col in self.data.columns for col in columns):
            raise ValueError("CSV файл должен содержать колонки: Date, Open, High, Low, Close, Adj Close, Volume")

    def graff(self):
        if self.data is None:
            raise ValueError("Данные не загружены")
    
        # Построение свечного графика с использованием нужных колонок
        mpf.plot(self.data[['Open', 'High', 'Low', 'Close']], type='candle', style='charles',
                 title='СТОИМОСТЬ АКЦИЙ APPLE', ylabel='ЦЕНА', volume=False)
        
    
if __name__ == "__main__":

    sp_csv = 'AAPL.csv'#путь к файлу
    app = Apple(sp_csv)
    
    
    try:
        app.dann()
        app.graff()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
