import json
from django.test import TestCase
from django.http import HttpRequest, JsonResponse
from .views import get_yesterdays_stock_prices, get_last_week_stock_prices, get_yesterdays_profitable_stocks


class TestStockPrices(TestCase):

    def test_yesterdays_stock_prices(self):

        stock_ticker = "AAPL"
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'stock_ticker': "AAPL"}

        response = get_yesterdays_stock_prices(request, stock_ticker)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)

        if data:
            self.assertIn('stock_name', data)
            self.assertIn('date', data)
            self.assertIn('high', data)
            self.assertIn('low', data)
            self.assertIn('pre_market', data)
            self.assertIn('close', data)

    def test_last_week_stock_prices(self):

        stock_ticker = "AAPL"
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'stock_ticker': 'AAPL'}

        response = get_last_week_stock_prices(request, stock_ticker)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        if data:
            self.assertIn('Stock Ticker', data)
            self.assertIn('No of days data', data)
            self.assertIn('Past Week Flow', data)
            self.assertIn('Average Volume Weighted Price', data)
            self.assertIn('Max price of the week', data)
            self.assertIn('Min Value of the week', data)

    def test_yesterdays_profitable_stocks(self):

        # stock_ticker = "AAPL"
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {}

        response = get_yesterdays_profitable_stocks(request)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

        if data:
            self.assertTrue(all('Stock Name' in stock for stock in data))
            self.assertTrue(all('Open' in stock for stock in data))
            self.assertTrue(all('Close' in stock for stock in data))
            self.assertTrue(all('Low' in stock for stock in data))
            self.assertTrue(all('High' in stock for stock in data))
            self.assertTrue(all('Volume' in stock for stock in data))
            self.assertTrue(all('Volume Weighted' in stock for stock in data))
            self.assertTrue(all('Profit' in stock for stock in data))





