from flask import Flask, request, jsonify
from auction import Auction
import asyncio
from websockets.server import serve
import threading
import time

import json

auctions = {}
websockets = []  # Store WebSocket connections

app = Flask(__name__)

@app.post("/cow")
async def cow_auction():
    if request.is_json:
        # TODO: Add query params (auction ID and endtime) to fwd msg
        auction_id = len(auctions)
        sleeptime = 5
        auction_json = request.get_json()
        await forward_auction(auction_json)

        # TODO create auction based on unique ID and set timer
        auctions[len(auctions)] = Auction(auction_json, auction_id, sleeptime)

        # TODO implement proper timing
        time.sleep(sleeptime)


        return auctions[auction_id].best_bid, 200
    return {"error": "Request must be JSON"}, 415

async def ping(websocket):
    while True:
        await websocket.send('{"message":"PING"}')
        print('------ ping')
        await asyncio.sleep(5)

async def receive_bids(websocket):
    # This gets latest auction
    # TODO: Implement a proper check on auction ID. Maybe create a seperate WS endpoint for each auction?
    auction_id = len(auctions)

    websockets.append(websocket)
    print(websockets)
    async for message in websocket:
        auctions[0].addBid(message)
        await websocket.send(message)

async def forward_auction(message):
    for ws in websockets:
        await ws.send(json.dumps(message))

async def websocket():
    async with serve(receive_bids, "localhost", 8765):
        task = asyncio.create_task(ping(websocket))
        await asyncio.Future()  # run forever

def restapi():
    app.run()

if __name__=='__main__':
    threading.Thread(target=restapi).start()
    asyncio.run(websocket())

