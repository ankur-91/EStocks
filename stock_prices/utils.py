from datetime import datetime, timedelta
import requests
import json


# If todays date is  Sunday or Monday, then get the date of Friday
def get_last_weekday(today):
    day_of_the_week = today.weekday()

    if day_of_the_week == 6:
        yesterdays_date = today - timedelta(days=2)
    elif day_of_the_week == 0:
        yesterdays_date = today - timedelta(days=3)
    else:
        yesterdays_date = today - timedelta(days=1)

    yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

    return yesterdays_date


def get_yesterdays_data(stock_ticker):
    BASE_URL = 'https://api.polygon.io/v1/'
    endpoint = 'open-close/'
    api_key = 'hzWJ74CR8eGXs1zUWwgA0Twj0qUQ9ycd'
    todays_date = datetime.now()
    yesterdays_date = get_last_weekday(todays_date)  # If todays date is  Sunday or Monday, then get the date of Friday

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    parameters = {
        'adjusted': True,
        'apiKey': api_key
    }

    url = BASE_URL + endpoint + stock_ticker + '/' + yesterdays_date
    response = requests.get(url=url, params=parameters, headers=headers)

    if response.status_code == 200:
        try:
            data = response.text
            parse_json = json.loads(data)
            return parse_json
        except ValueError as e:
            print(f'Exception: {e}')
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def get_yesterdays_polygon_profit_data():
    BASE_URL = 'https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/'
    api_key = 'hzWJ74CR8eGXs1zUWwgA0Twj0qUQ9ycd'
    todays_date = datetime.now()
    yesterdays_date = get_last_weekday(todays_date)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    parameters = {
        'adjusted': True,
        'apiKey': api_key,
    }

    url = BASE_URL + yesterdays_date
    print(f'url: {url}')
    try:
        response = requests.get(url=url, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])

    except requests.exceptions.RequestException as e:
        print(f'HTTP Request failed: {e}')
    except ValueError as e:
        print(f'JSON parsing error: {e}')

    return []


def get_last_week_data(stock_ticker):
    BASE_URL = 'https://api.polygon.io/v2/aggs/ticker/'
    api_key = 'hzWJ74CR8eGXs1zUWwgA0Twj0qUQ9ycd'
    todays_date = datetime.now()
    past_week_date = todays_date - timedelta(days=7)
    past_week_date = past_week_date.strftime('%Y-%m-%d')
    todays_date = todays_date.strftime('%Y-%m-%d')

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    parameters = {
        'adjusted': True,
        'apiKey': api_key,
        'sort': 'asc',

    }

    url = BASE_URL + stock_ticker + '/range/1/day/' + past_week_date + '/' + todays_date
    response = requests.get(url=url, params=parameters, headers=headers)

    if response.status_code == 200:
        try:
            data = response.text
            parse_json = json.loads(data)
            return parse_json
        except ValueError as e:
            print(f'Exception: {e}')
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
