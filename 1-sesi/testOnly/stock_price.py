# cheking stock price using python
import yfinance as yf

STK = input("Enter share name : ")

data = yf.Ticker(STK).history(period = "1d")

last_market_price = data["Close"].iloc[-1]

print("last market price : ",last_market_price)