from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

STOCKS = {
    "RELIANCE": "Reliance Industries Limited",
    "HDFCBANK": "HDFC Bank Limited",
    "BHARTIARTL": "Bharti Airtel Limited",
    "ICICIBANK": "ICICI Bank Limited",
    "SBIN": "State Bank of India",
    "TCS": "Tata Consultancy Services Limited",
    "INFY": "Infosys Limited",
    "LT": "Larsen & Toubro Limited",
    "HINDUNILVR": "Hindustan Unilever Limited",
    "BAJFINANCE": "Bajaj Finance Limited",
}

def get_stock_data():
    results = []

    for symbol, company in STOCKS.items():
        try:
            ticker = yf.Ticker(f"{symbol}.NS")
            info = ticker.fast_info

            results.append({
                "symbol": symbol,
                "company": company,
                "current_price": info.get("lastPrice"),
                "previous_close": info.get("previousClose"),
                "day_high": info.get("dayHigh"),
                "day_low": info.get("dayLow"),
                "volume": info.get("lastVolume"),
            })
        except Exception as e:
            results.append({
                "symbol": symbol,
                "company": company,
                "error": str(e)
            })

    return {
        "success": True,
        "count": len(results),
        "data": results
    }

@app.route("/")
def home():
    return jsonify({"message": "API is running"})

@app.route("/stocks")
def stocks():
    return jsonify(get_stock_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)