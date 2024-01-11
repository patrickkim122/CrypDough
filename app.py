from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS
import config
import csv
import talib
import numpy as np

from binance.client import Client
from binance.enums import *

app = Flask(__name__)
CORS(app)
app.secret_key = b'uhjewgbfhjewgfjhewsbfjherwgtfuyhewbfhujewrgfyuiweggf'

client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():
    title = 'CrypDough'
    
    info = client.get_account()

    balances = info['balances']
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('indexNP.html', title=title, balances=balances, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_test_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity']
        )
    except Exception as e:
        flash(e.message, "error")
    return redirect('/')

@app.route('/trades')
def trades():
    trades = client.get_my_trades(symbol='BTCUSDT')
    return trades

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")

    pretty_candles = []
    for candle in candles:
        pretty_candle = {
            "time": candle[0] / 1000,
            "open": candle[1],
            "high": candle[2],
            "low": candle[3],
            "close": candle[4]
        }
        pretty_candles.append(pretty_candle)
    
    # candle_dict = jsonify(pretty_candles)
    return jsonify(pretty_candles)

