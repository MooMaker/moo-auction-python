import asyncio
from websockets.server import serve

import json

class MarketMakerWebsocket:
    def __init__(self):
        self.auctions = {} #TODO move this to seperate module or use a database
        self.connections = [] # Store WebSocket connections


    async def ping(self):
        while True:
            await self.websocket.send('{"message":"PING"}')
            print('------ ping')
            await asyncio.sleep(5)

    async def receive_bids(self, connection):
        # This gets latest auction
        # TODO: Implement a proper check on auction ID. Maybe create a seperate WS endpoint for each auction?
        auction_id = len(self.auctions)

        # TODO: Move this to seperate connection management function (also manage disconnects)
        self.connections.append(connection)
        print(self.connections)


        async for message in connection:
            self.auctions[0].addBid(message)
            await connection.send(message)

    async def forward_auction(self, message):
        for ws in self.connections:
            await ws.send(json.dumps(message))

    async def websocket(self):
        async with serve(self.receive_bids, "localhost", 8765):
            task = asyncio.create_task(self.ping())
            await asyncio.Future()  # run forever