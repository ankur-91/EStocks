# EStocks

This app will show the performance of your favourite stocks and will show list top 5 profitable tiocks from yesterday. This app is currently hosted at localhost.
To achieve this, I have created 3 API endpoints:

1. http://localhost:8000/api/AAPL/ # This API will show the yesterday's performance of Apple(APPLE) stock. It displays the following details: Stock Name, Date, High, Low, Pre Market, Open, Close.
2. http://localhost:8000/api/AAPL/past_week/ # This API will show how Apple(APPL) stock performed last week: Stock Name, High, Low, Open, Close, Volume Weighted and Profit(particular day) 
3. http://localhost:8000/api/all_stocks/top_stocks/ # This API will show the yesterday's top 5 stocks based on the maximum profit  
