import backtrader as bt
import matplotlib
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)

        if self.rsi > 70 and self.position:
            self.close()

cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2020-07-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2023-12-31', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='data/BTCUSDT_2015-2023_1Day.csv', dtformat=2, compression=1, timeframe=bt.TimeFrame.Days, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()

