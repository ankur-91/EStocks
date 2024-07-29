# EStocks

This app will show the performance of your favourite stocks and will show list top 5 profitable tiocks from yesterday. This app is currently hosted at localhost.
To achieve this, I have created 3 API endpoints:

1. http://localhost:8000/api/AAPL/ # This API will show the yesterday's performance of Apple(APPLE) stock. It displays the following details: Stock Name, Date, High, Low, Pre Market, Open, Close.
2. http://localhost:8000/api/AAPL/past_week/ # This API will show how Apple(APPL) stock performed last week: Stock Name, High, Low, Open, Close, Volume Weighted and Profit(particular day) 
3. http://localhost:8000/api/all_stocks/top_stocks/ # This API will show the yesterday's top 5 stocks based on the maximum profit  

To run the application from your machine, clone this repo and follow below steps:

1. Start virtual environment by using this command: source/bin/activate if you are Linux user or use venv\Scripts\activate if you are Windows user
3. Run this command from your repo: python manage.py runserver
4. Use any of the above listed APIs on your browser to view the stock data
