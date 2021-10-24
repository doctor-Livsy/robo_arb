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



if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(settings=load_settings()))
