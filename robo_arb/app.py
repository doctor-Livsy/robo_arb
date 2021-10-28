import asyncio
import configparser
from exchanges_streaming import start_sockets, exchanges_message_handler


def load_settings() -> configparser.ConfigParser:
    """
    Function loads settings from settings.ini file.

    :return: config: instance of ConfigParser
    """

    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config


async def exchanges_websocket_data(bnc_ticker: str, ftx_ticker: str) -> dict:
    """
    Function create dict of Websockets connection info for two exchanges.

    :param bnc_ticker: Binance ticker
    :param ftx_ticker: FTX ticker
    :return: websocket_data: dict
    """

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
    """
    Main function. After loading settings it run Websockets connection and
    subscribe to exchange updates.
    There is handling updates and executing strategy also.

    :param settings: settings from settings.ini file
    :return: None
    """

    # extraction of settings
    bnc_ticker = settings['ticker_parameters']['bnc_ticker']
    ftx_ticker = settings['ticker_parameters']['ftx_ticker']
    param = {'r_r': float(settings['system_parameters']['refresh_rate']),
             'p_d': float(settings['system_parameters']['price_difference']),
             'm': float(settings['system_parameters']['margin'])}

    # opening websockets and subscribing to update
    websocket_data = await exchanges_websocket_data(bnc_ticker, ftx_ticker)
    bnc, ftx = await start_sockets(websocket_data)

    # processing updates
    await exchanges_message_handler(bnc, ftx, param)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(settings=load_settings()))
