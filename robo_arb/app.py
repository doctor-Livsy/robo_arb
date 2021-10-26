import asyncio
import configparser
from exchanges_streaming import start_sockets, exchanges_message_handler


def load_settings() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config


async def exchanges_websocket_data(bnc_ticker: str, ftx_ticker: str) -> dict:
    binance_data = {'url': f'wss://stream.binance.com:9443/ws/{bnc_ticker}@bookTicker',
                    'subscribe_request': {"method": "SUBSCRIBE",
                                          "params": [bnc_ticker.lower() + "@bookTicker"],
                                          "id": 1}}
    ftx_data = {'url': f'wss://ftx.com/ws/',
                'subscribe_request': {'op': 'subscribe',
                                      'channel': 'ticker',
                                      'market': ftx_ticker}}
    websocket_data = {'binance': binance_data,
                      'ftx': ftx_data}
    return websocket_data


async def main(settings: configparser.ConfigParser) -> None:
    # loading of settings
    bnc_ticker = settings['ticker_parameters']['bnc_ticker']
    ftx_ticker = settings['ticker_parameters']['ftx_ticker']
    refresh_rate = float(settings['system_parameters']['refresh_rate'])
    price_diff = float(settings['system_parameters']['price_difference'])

    # opening websockets and subscribing to update
    websocket_data = await exchanges_websocket_data(bnc_ticker, ftx_ticker)
    bnc, ftx = await start_sockets(websocket_data)

    # processing updates
    await exchanges_message_handler(bnc, ftx, refresh_rate, price_diff)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(settings=load_settings()))
