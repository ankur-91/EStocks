from django.urls import path
from .views import get_yesterdays_stock_prices, get_last_week_stock_prices, get_yesterdays_profitable_stocks

urlpatterns = [
    path('<str:stock_ticker>/', get_yesterdays_stock_prices, name='get_yesterdays_stock_prices'),
    path('<str:stock_ticker>/past_week/', get_last_week_stock_prices, name='get_last_week_stock_prices'),
    path('all_stocks/top_stocks/', get_yesterdays_profitable_stocks, name='get_yesterdays_profitable_stocks')
]