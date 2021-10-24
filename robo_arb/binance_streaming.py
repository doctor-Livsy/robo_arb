import asyncio
import binance


async def start_binance_socket(ticker: str):
    # client = await binance.AsyncClient.create()
    # bm = binance.BinanceSocketManager(client)
    #
    # # start any sockets here, i.e a trade socket
    # ts = bm.aggtrade_socket('btcusdt')
    # # then start receiving messages
    # async with ts as tscm:
    #     while True:
    #         res = await tscm.recv()
    #         print(res)
    # await client.close_connection()




# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_binance_socket(ticker='BNBBTC'))
