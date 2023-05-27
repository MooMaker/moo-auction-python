import asyncio
import threading
import time

from flask import Flask, request

from auction import Auction
from market_maker_websocket import MarketMakerWebsocket

marketmakerwebsocket = MarketMakerWebsocket()

app = Flask(__name__)

@app.post("/cow/auction")
async def cow_auction():
    if request.is_json:
        auction_json = request.get_json()
        auction_id = auction_json["metadata"]["auction_id"]
        print(auction_id)
        await marketmakerwebsocket.forward_auction(auction_json)
        marketmakerwebsocket.auctions[auction_id] = Auction(auction_json)

        # TODO implement proper timing
        print(auction_json["metadata"]["time_limit"])
        time.sleep(auction_json["metadata"]["time_limit"])

        return marketmakerwebsocket.auctions[auction_id].best_bid, 200
    return {"error": "Request must be JSON"}, 415

@app.post("/cow/results")
async def result():
    if request.is_json:
        results_json = request.get_json()
        auction_id  = results_json["auction_id"]
        win = results_json["win"] # TODO: win should be a boolean. confirm what data format we receive from solver/CoW
        await marketmakerwebsocket.publish_results(auction_id, win)
        return {}, 204
    return {"error": "Request must be JSON"}, 415

def restapi():
    app.run()

if __name__=='__main__':
    threading.Thread(target=restapi).start()
    asyncio.run(marketmakerwebsocket.websocket())

