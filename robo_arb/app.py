import asyncio
import configparser
from binance_streaming import start_binance_socket


def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config


async def main(settings: configparser.ConfigParser):
    ticker = settings['ticker_parameters']['ticker']
    binance_socket = await start_binance_socket(ticker)
    print(0)

if __name__ == '__main__':
    base_loop = asyncio.get_running_loop()
    base_loop.run_until_complete(main(settings=load_settings()))
