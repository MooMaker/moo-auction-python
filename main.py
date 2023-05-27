from flask import Flask, request, jsonify
from auction import Auction
from market_maker_websocket import MarketMakerWebsocket
import asyncio
import threading
import time

marketmakerwebsocket = MarketMakerWebsocket()

app = Flask(__name__)

@app.post("/cow/auction")
async def cow_auction():
    if request.is_json:
        # TODO: Do validation on query params (REQUIRED)
        auction_json = request.get_json()
        auction_id  = int(request.args.get("auction_id"))
        end_time = request.args.get("end_time")
        auction_json["auction_id"] = auction_id
        auction_json["end_time"] = end_time
        await marketmakerwebsocket.forward_auction(auction_json)

        # TODO create auction for each order (group under auction_id)
        marketmakerwebsocket.auctions[auction_id] = Auction(auction_json)

        # TODO implement proper timing

        sleeptime = 5
        time.sleep(sleeptime)

        return marketmakerwebsocket.auctions[auction_id].best_bid, 200
    return {"error": "Request must be JSON"}, 415

@app.post("/cow/results")
async def result():
    if request.is_json:
        auction_json = request.get_json()
        auction_id  = auction_json["auction_id"]
        results = auction_json["results"]
        if (results):
            print("informing winning MMs")
        else:
            print("no winner")
        return {}, 204
    return {"error": "Request must be JSON"}, 415

def restapi():
    app.run()

if __name__=='__main__':
    threading.Thread(target=restapi).start()
    asyncio.run(marketmakerwebsocket.websocket())

