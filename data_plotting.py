import matplotlib.pyplot as plt
import pandas as pd
from Available_style import available_styles

def create_and_save_plot(data, ticker, period, filename=None, style=None):
    plt.figure(figsize=(10, 6))

    if style in available_styles:
        plt.style.use(style)  # Применение выбранного стиля к графику
    else:
        print(f"Стиль '{style}' не найден. Используйте стили по умолчанию.")

    if 'Date' not in data:
        #проверяет, является ли индекс данных столбцом с временными метками.
        if pd.api.types.is_datetime64_any_dtype(data.index):
            #преобразование индекса DataFrame data в массив NumPy
            dates = data.index.to_numpy()
            #добавление линий
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['RSI'].values, label='RSI', color='green')
            plt.plot(dates, data['MACD'].values, label='MACD', color='red')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            #преобразует столбец 'Date' в DataFrame 'data' в столбец с временными метками, используя функцию
            data['Date'] = pd.to_datetime(data['Date'])
        #построение графиков из двух массивов метода 'plot' массив временных меток и массив закрытия цен
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['RSI'], label='RSI')
        plt.plot(data['Date'], data['MACD'], label='MACD', color='orange')

    #построение графика по х и у и название
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    #добавление картинки на график
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
