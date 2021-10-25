import websockets
import json


async def exchange_message_handler(websocket: websockets.WebSocketClientProtocol):
    async for message in websocket:
        print(message)


async def start_socket(url, request):
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps(request))
        await exchange_message_handler(websocket)
