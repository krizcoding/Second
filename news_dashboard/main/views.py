from django.shortcuts import render
from .utils import fetch_news, fetch_weather, fetch_stock

def home(request):
    news_articles = fetch_news()
    weather_data = fetch_weather()
    stock_data = fetch_stock()

    # Extract stock price safely
    stock_price = None
    try:
        time_series = stock_data.get("Time Series (5min)", {})
        latest_timestamp = sorted(time_series.keys())[-1]  # Get the latest timestamp
        stock_price = time_series[latest_timestamp]["1. open"]
    except (KeyError, IndexError, TypeError):
        stock_price = "Data not available"

    context = {
        "news": news_articles[:5],  # Limit to 5 articles
        "weather": weather_data,
        "stock_price": stock_price,
    }
    return render(request, "main/home.html", context)

