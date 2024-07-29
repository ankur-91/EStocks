from django.shortcuts import render
from .utils import get_yesterdays_data, get_last_week_data, get_yesterdays_polygon_profit_data
from django.http import JsonResponse


def get_yesterdays_stock_prices(request, stock_ticker):

    # Get the stock data from yesterday
    polygon_data = get_yesterdays_data(stock_ticker)
    if polygon_data is None:
        return JsonResponse({'error': 'Failed to retrieve data or no data available'}, status=500)

    stock_info = {
        'Stock Name': polygon_data.get('symbol', 'N/A'),
        'Date': polygon_data.get('from', 'N/A'),
        'High': polygon_data.get('high', 'N/A'),
        'Low': polygon_data.get('low', 'N/A'),
        'Pre Market': polygon_data.get('preMarket', 'N/A'),
        'Open': polygon_data.get('open', 'N/A'),
        'Close': polygon_data.get('close', 'N/A')
    }

    return JsonResponse(stock_info)


def get_yesterdays_profitable_stocks(request):
    try:
        all_top_stocks = []
        # Call polygon.io api to get data of all the stocks from yesterday
        results = get_yesterdays_polygon_profit_data()

        # get top 5 stocks based on Profit value
        if results:
            for stock in results:
                profit = stock['c'] - stock['o']
                stock['profit'] = round(profit, 2)
            profit_data = sorted(results, key=lambda x: x['profit'], reverse=True)
            top_five_stocks = profit_data[:5]

            # Update the value to more readable strings so that the values are more readable
            for t_stocks in top_five_stocks:
                stock_info = {'Stock Name': t_stocks['T'],
                              'Open': t_stocks['o'],
                              'Close': t_stocks['c'],
                              'Low': t_stocks['l'],
                              'High': t_stocks['h'],
                              'Volume': t_stocks['v'],
                              'Volume Weighted': t_stocks['vw'],
                              'Profit': t_stocks['profit']}
                all_top_stocks.append(stock_info)

            return JsonResponse(all_top_stocks, safe=False)
        else:
            return JsonResponse({"error": "No data available"}, status=404)
    except Exception as e:
        print(f"Error occurred: {e}")
        return JsonResponse({"error": "Failed to retrieve data"}, status=500)


def get_last_week_stock_prices(request, stock_ticker):
    total_vw_average_price = 0
    high_prices = []
    low_prices = []

    # get the values of the stock from past week
    polygon_data = get_last_week_data(stock_ticker)
    results = polygon_data['results']

    # For each day calculate the percentage change based on closing and opening value of the day
    for day in results:
        total_vw_average_price += day['vw']
        high_prices.append(day['h'])
        low_prices.append(day['l'])
        percentage_change_calculation = ((day['c'] - day['o']) / day[
            'o']) * 100  # ((closing price - opening price) / opening price) * 100
        day['percentage_change'] = str(round(percentage_change_calculation, 2)) + '%'

    # Find the max high and min low from the 5 days
    max_high = round(max(high_prices), 2)
    min_low = round(min(low_prices), 2)

    # Find the average of the volume weighted value from all 5 days
    average_vw_price = round(total_vw_average_price / len(results), 2)

    result_data = polygon_data.get('results', 'N/A')
    final_past_week_data = []

    # Update the value to more readable strings so that the values are more readable
    if result_data:
        for day in result_data:
            stock_info = {'Open': day['o'],
                          'Close': day['c'],
                          'Low': day['l'],
                          'High': day['h'],
                          'Volume': day['v'],
                          'Volume Weighted': day['vw'],
                          'Percentage Change': day['percentage_change']}
            final_past_week_data.append(stock_info)

    response = {
        'Stock Ticker': stock_ticker,
        'No of days data': polygon_data.get('resultsCount', 'N/A'),
        'Past Week Flow': final_past_week_data,
        'Average Volume Weighted Price': average_vw_price,
        'Max price of the week': max_high,
        'Min Value of the week': min_low
    }

    return JsonResponse(response, safe=False)
