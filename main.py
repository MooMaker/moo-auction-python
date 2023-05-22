from flask import Flask, request, jsonify
from auction import Auction
from market_maker_websocket import MarketMakerWebsocket
import asyncio
import threading
import time


marketmakerwebsocket = MarketMakerWebsocket()

app = Flask(__name__)

@app.post("/cow")
async def cow_auction():
    if request.is_json:
        # TODO: Add query params (auction ID and endtime) to fwd msg
        auction_id = len(marketmakerwebsocket.auctions)
        sleeptime = 5
        auction_json = request.get_json()
        await marketmakerwebsocket.forward_auction(auction_json)

        # TODO create auction based on unique ID and set timer
        marketmakerwebsocket.auctions[len(marketmakerwebsocket.auctions)] = Auction(auction_json, auction_id, sleeptime)

        # TODO implement proper timing
        time.sleep(sleeptime)


        return marketmakerwebsocket.auctions[auction_id].best_bid, 200
    return {"error": "Request must be JSON"}, 415

def restapi():
    app.run()

if __name__=='__main__':
    threading.Thread(target=restapi).start()
    asyncio.run(marketmakerwebsocket.websocket())

