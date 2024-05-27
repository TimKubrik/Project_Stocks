import plotly.graph_objects as go
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None, style=None):
    fig = go.Figure()

    if 'Date' not in data:
        # проверяет, является ли индекс данных столбцом с временными метками.
        if pd.api.types.is_datetime64_any_dtype(data.index):
            # преобразование индекса DataFrame data в массив NumPy
            dates = data.index
            # добавление линий
            fig.add_trace(go.Scatter(x=dates, y=data['Close'], mode='lines', name='Close Price'))
            fig.add_trace(go.Scatter(x=dates, y=data['Moving_Average'], mode='lines', name='Moving Average'))
            fig.add_trace(go.Scatter(x=dates, y=data['RSI'], mode='lines', name='RSI'))
            fig.add_trace(go.Scatter(x=dates, y=data['MACD'], mode='lines', name='MACD'))
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            # преобразует столбец 'Date' в DataFrame 'data' в столбец с временными метками, используя функцию
            data['Date'] = pd.to_datetime(data['Date'])
        # построение графиков из двух массивов метода 'plot' массив временных меток и массив закрытия цен
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close Price'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Moving_Average'], mode='lines', name='Moving Average'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['RSI'], mode='lines', name='RSI'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['MACD'], mode='lines', name='MACD'))

    # построение графика по х и у и название
    fig.update_layout(
        title=f"{ticker} Цена акций с течением времени",
        xaxis_title="Дата",
        yaxis_title="Цена",
        xaxis_type='date'
    )

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.html"

    fig.write_html(filename)
    print(f"График сохранен как {filename}")
