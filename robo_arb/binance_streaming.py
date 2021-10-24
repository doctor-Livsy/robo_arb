import asyncio
import websockets
import json

async def start_binance_socket(ticker: str):
    # TODO: Надо перейти на версию python 3.8.8
    url = 'wss://stream.binance.com:9443/ws/<streamName>'
    subscribe_request = {"method": "SUBSCRIBE",
                         "params": [ticker + "@aggTrade"],
                         "id": 1}

    async with websockets.connect(url) as websocket:
        await websocket.send(subscribe_request)
        greeting = await websocket.recv()
        print(greeting)



# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_binance_socket(ticker='BNBBTC'))

