import yfinance as yf
import pandas as pd

# NSE Stock symbols
stocks = {
    "RELIANCE": "Reliance Industries Limited",
    "HDFCBANK": "HDFC Bank Limited",
    "BHARTIARTL": "Bharti Airtel Limited",
    "ICICIBANK": "ICICI Bank Limited",
    "SBIN": "State Bank of India",
    "TCS": "Tata Consultancy Services Limited",
    "INFY": "Infosys Limited",
    "LT": "Larsen & Toubro Limited",
    "HINDUNILVR": "Hindustan Unilever Limited",
    "BAJFINANCE": "Bajaj Finance Limited"
}

results = []

for symbol, company in stocks.items():
    ticker = yf.Ticker(symbol + ".NS")
    info = ticker.fast_info

    try:
        current_price = info.get("lastPrice")
        previous_close = info.get("previousClose")
        day_high = info.get("dayHigh")
        day_low = info.get("dayLow")
        volume = info.get("lastVolume")

        results.append({
            "Symbol": symbol,
            "Company": company,
            "Current Price": current_price,
            "Previous Close": previous_close,
            "Day High": day_high,
            "Day Low": day_low,
            "Volume": volume
        })

    except Exception as e:
        print(f"Error fetching {symbol}: {e}")

df = pd.DataFrame(results)

print(df)

# Optional: Save to CSV
df.to_csv("nse_stock_prices.csv", index=False)