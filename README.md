# CrypDough

CrypDough is a trading software that utilises the Binance API to analyse and trade cryptocurrencies.

The first constituent has the following functionalities:
- CrypDough GUI consisting of candlestick charts for selected cryptocurrencies
- Account balance for connected account
- Buy/Sell mechanism
- Basic RSI indicators to facilitate decision making

The second part of CrypDough is named Smart CrypDough. It is a trading bot that uses the Binance API to determine good entry points for Buy/Sell Market orders.
- Current indicators implemented include the MACD and RSI indicators
- Packages used include TA-Lib (Technical Analysis of stocks) and websocket/json, as well as a Binance wrapper package.

Through the use of this code, with a starting amount of $100 AUD and start time of 01/01/2024, Smart CrypDough traded INJUSDT with a profit of $30, including commission fees.
