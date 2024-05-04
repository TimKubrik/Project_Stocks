import data_download as dd
import data_plotting as dplt
import schedule_actions as shd


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
    period_date = input("Хотите выбрать конкретные даты? yes/no: ")


    if period_date.lower()=='yes':
        start_date = input('Введите начало даты для анализа(например 2023-02-23):')
        end_date = input('Введите конец даты для анализа(например 2023-03-23):')
        period = None
    else:
        start_date = None
        end_date = None
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Получение данных
    stock_data = dd.fetch_stock_data(ticker, start_date, end_date, period)


    #Расчет и построение графика RSI
    stock_data = dd.add_rsi(stock_data)

    #Расчет и построение графика MACD
    stock_data = dd.add_macd(stock_data)

    # Добавление скользящей средней к данным
    stock_data = dd.add_moving_average(stock_data)

    # Создание данных на графике
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Вычисление и вывод средней цены закрытия
    shd.calculate_and_display_average_price(stock_data)

    #Уведомление пользователя, если цена акций колебалась более чем на заданный процент за период
    shd.notify_if_strong_fluctuations(stock_data, 5)

    #Сохранение данных в CSV файле и экспорт данных
    shd.export_data_to_csv(stock_data, 'output.csv')



if __name__ == "__main__":
    main()
