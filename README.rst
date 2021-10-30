**Arbitration trade robot**
===========================

The asynchronous Robot connect to Binance and FTX exchanges by Websockets connection,
subscribe on updates selected tickers and execute arbitration strategy.

Now the robot terminated by restarting the terminal.

Input parameters modify in 'env.list' file and selected in docker containers
with command: "docker run --env-file ./param.list <name_robot_image>".

env.list contains 5 parameters:

* BINANCE_TICKER : Binance exchange ticker (without quotation marks)
* FTX_TICKER : FTX exchange ticker (without quotation marks)
* REFRESH_RATE : Update frequency of order books (default: 0.01s)
* PRICE_DIFFERENCE : Minimal tickers price difference between exchanges
* MARGIN : Margin value for execute trades (in USDT or BTC)