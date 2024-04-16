import matplotlib.pyplot as plt
import pandas as pd

def calculate_and_display_average_price(data):
    #Средняя цена закрытия акций за заданный период с помощью метода mean()
    mean_close_price = data['Close'].mean()
    #Вывод цены закрытия c точностью до 2-х знаков
    print(f"Средняя цена закрытия: {mean_close_price:.2f}")

def notify_if_strong_fluctuations(data, threshold):
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    price_difference = max_price - min_price
    percentage = (price_difference / min_price) * 100

    if percentage > threshold:
        print(f"Цена акций колебалась на {percentage:.2f}% за период, что превышает порог в {threshold}%.")

def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        #проверяет, является ли индекс данных столбцом с временными метками.
        if pd.api.types.is_datetime64_any_dtype(data.index):
            #преобразование индекса DataFrame data в массив NumPy
            dates = data.index.to_numpy()
            #добавление линий
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
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
    #построение графика по х и у и название
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    #добавление легенды на график
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
