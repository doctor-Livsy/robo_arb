import asyncio
import websockets
import json
from websockets import ConnectionClosed
from strategy import price_analyze


async def exchanges_message_handler(bnc_websocket, ftx_websocket, param) -> None:
    """
    The function processes exchange updates and translates them into the "price_analyze" function

    :param bnc_websocket: Binance websocket object
    :param ftx_websocket: FTX Websocket object
    :param param: contains refresh rate, price diff and trade volume
    :return: None
    """

    ok = True
    while ok:
        try:
            # receiving updates
            bnc = await bnc_websocket.recv()
            ftx = await ftx_websocket.recv()
            # translate to execute strategy
            await price_analyze(json.loads(bnc), json.loads(ftx), param['p_d'], param['m'])
            # sleep if its needed
            await asyncio.sleep(param['r_r'])

        except ConnectionClosed:
            print('Connection Closed. Need to reboot.')
            ok = False


async def start_sockets(data: dict) -> tuple:
    """
    The function create Websockets connections and subscribe to updates.

    :param data:
    :return: tuble of bnc_websocket and ftx_websocket objects
    """

    # create Websockets connections
    bnc_websocket = await websockets.connect(data['binance']['url'], max_queue=None, ping_interval=None)
    ftx_websocket = await websockets.connect(data['ftx']['url'], max_queue=None, ping_interval=None)

    # subscribing to updates
    await bnc_websocket.send(json.dumps(data['binance']['subscribe_request']))
    await ftx_websocket.send(json.dumps(data['ftx']['subscribe_request']))

    return bnc_websocket, ftx_websocket
