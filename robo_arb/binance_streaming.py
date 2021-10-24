import asyncio
import websockets
import json

async def start_binance_socket(ticker: str):

    url = f'wss://stream.binance.com:9443/ws/{ticker}@bookTicker'
    subscribe_request = {"method": "SUBSCRIBE",
                         "params": [ticker.lower() + "@bookTicker"],
                         "id": 1}

    ws = await websockets.connect(url)
    await ws.send(json.dumps(subscribe_request))
    message = await ws.recv()
    print(message)


async def binance_ws(ticker: str):
    print(0)


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_binance_socket(ticker='BNBBTC'))

