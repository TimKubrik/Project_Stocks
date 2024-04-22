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

def export_data_to_csv(data, filename):
    #Преобразование в DataFrame
    df = pd.DataFrame(data)
    #экспортируем DataFrame в файл CSV
    df.to_csv('output.csv', encoding='utf8')


