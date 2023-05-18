#!/usr/bin/env python


# #!/usr/bin/env python
# import asyncio
# import websockets
# from auction import Auction
#
# async def createOrderData(rawData):
#     orderdata = rawData
#     uri = "ws://localhost:8766"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(orderdata)
#
# async def hello(websocket):
#
#
#     async with websockets.connect(uri) as websocket:
#
#         orderdata = await websocket.recv()
#
#
#
# async def main():
#
#     async with websockets.serve(hello, "localhost", 8765):
#
#         await asyncio.Future()  # run forever
#
#
# if __name__ == "__main__":
#
#     asyncio.run(main())