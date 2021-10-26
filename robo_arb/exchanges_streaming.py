import asyncio
import websockets
import json
from websockets import ConnectionClosed
from exchanges_buffer import price_analyze


async def exchanges_message_handler(bnc_websocket, ftx_websocket, refresh_rate, diff) -> None:

    ok = True
    while ok:
        try:

            bnc = await bnc_websocket.recv()
            ftx = await ftx_websocket.recv()
            await price_analyze(json.loads(bnc), json.loads(ftx), diff)
            await asyncio.sleep(refresh_rate)

        except ConnectionClosed:
            print('Connection Closed. Need to reboot.')
            ok = False


async def start_sockets(data: dict, refresh_rate, diff) -> None:

    bnc_websocket = await websockets.connect(data['binance']['url'], max_queue=None, ping_interval=None)
    ftx_websocket = await websockets.connect(data['ftx']['url'], max_queue=None, ping_interval=None)

    await bnc_websocket.send(json.dumps(data['binance']['subscribe_request']))
    await ftx_websocket.send(json.dumps(data['ftx']['subscribe_request']))

    await exchanges_message_handler(bnc_websocket, ftx_websocket, refresh_rate, diff)




