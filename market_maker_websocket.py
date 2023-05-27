import asyncio
from websockets.server import serve

import json

class MarketMakerWebsocket:
    def __init__(self):
        self.auctions = {} #TODO: move this to seperate module or use a database
        self.connections = [] # Store WebSocket connections


    async def ping(self):
        while True:
            await self.websocket.send('{"message":"PING"}')
            print('------ ping')
            await asyncio.sleep(5)

    async def receive_bids(self, connection):
        # This gets latest auction
        # TODO: Implement a proper check on auction ID.
        #  Maybe create a seperate WS endpoint for each auction? (faster)
        #  or auctionid as field (slower)
        auction_id = len(self.auctions)

        # TODO: Move this to seperate connection management function (also manage disconnects)
        self.connections.append(connection)
        print(self.connections)


        async for message in connection:
            auction_id = 0
            order_id = 0
            new_bid = json.loads(message)
            try:
                self.auctions[auction_id].addBid(order_id, new_bid)
                await connection.send("received bid")
            except (KeyError):
                # Todo: error handling when order_id is wrong
                await connection.send("ERROR: These is no auction with auctionId " + str(auction_id))

    async def forward_auction(self, message):
        for ws in self.connections:
            await ws.send(json.dumps(message))

    async def websocket(self):
        async with serve(self.receive_bids, "localhost", 8765):
            task = asyncio.create_task(self.ping())
            await asyncio.Future()  # run forever