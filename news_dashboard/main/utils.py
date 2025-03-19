import requests
from django.utils.timezone import settings

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.NEWS_API_KEY}"
    response = requests.get(url).json()
    return response.get('articles', [])

def fetch_weather(city="London"):
    url = f"https://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={city}&aqi=no"
    response = requests.get(url).json()
    return response

def fetch_stock(symbol="AAPL"):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={settings.STOCK_API_KEY}"
    response = requests.get(url).json()
    return response
