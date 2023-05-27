import asyncio
import json

from websockets.server import serve


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

        # TODO: Move this to seperate connection management function (also manage disconnects)
        self.connections.append(connection)
        print(self.connections)


        async for message in connection:
            # TODO: Implement a proper check on auction ID.
            auction_id = 0
            received_bids = json.loads(message)
            try:
                self.auctions[auction_id].parse_bids(received_bids)
                await connection.send("received bids")
            except (KeyError):
                # Todo: error handling when order_id is wrong
                await connection.send("ERROR: No auction exists with auctionId " + str(auction_id))

    async def forward_auction(self, message):
        for ws in self.connections:
            await ws.send(json.dumps(message))

    async  def publish_results(self, auction_id, win):
        results = {}
        if (win):
            results = self.auctions[auction_id].get_results()

        print(results)
        for ws in self.connections:
            await ws.send(json.dumps(results))

    async def websocket(self):
        async with serve(self.receive_bids, "localhost", 8765):
            task = asyncio.create_task(self.ping())
            await asyncio.Future()  # run forever