import config
import csv
import talib
import numpy as np

from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()


# for price in prices:
#     print(price)

# file = open('BTCUSDT_15minutes.csv', 'w', newline='')

# candlewriter = csv.writer(file, delimiter=',')


# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
# for candle in candles:
#     print(candle)
#     candlewriter.writerow(candle)

file = open('data/BTCUSDT_2015-2023_15Minute.csv', 'w', newline='')

candlewriter = csv.writer(file, delimiter=',')

candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2015", "31 Dec, 2023")
for candle in candles:
    candle[0] = candle[0] / 1000
    candlewriter.writerow(candle)

print("Historical data has been extracted!")
