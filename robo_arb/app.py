import asyncio
import configparser
from exchanges_streaming import start_socket


def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config


async def binance_init(ticker):
    url = f'wss://stream.binance.com:9443/ws/{ticker}@bookTicker'
    subscribe_request = {"method": "SUBSCRIBE",
                         "params": [ticker.lower() + "@bookTicker"],
                         "id": 1}
    await start_socket(url=url, request=subscribe_request)


async def ftx_init(ticker):
    url = f'wss://ftx.com/ws/'
    subscribe_request = {'op': 'subscribe',
                         'channel': 'orderbook',
                         'market': 'BTC-PERP'}
    await start_socket(url=url, request=subscribe_request)


async def main(settings: configparser.ConfigParser):
    ticker = settings['ticker_parameters']['ticker']
    # await binance_init(ticker)
    await ftx_init(ticker)
    print(0)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(settings=load_settings()))
