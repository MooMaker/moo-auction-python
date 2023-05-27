class Auction:

    def __init__(self, json):
        self.json = json
        self.id = json["metadata"]["auction_id"]
        # self.end_time = json["end_time"]
        # TODO: add end_time
        self.is_sell_order = {}
        self.best_bid = {}
        for order_id in json["orders"]:
            self.is_sell_order[int(order_id)] = json["orders"][order_id]["is_sell_order"];
            self.best_bid[int(order_id)] = {}

    def parse_bids(self, market_maker_response):
        for order_id in market_maker_response:
            self.add_bid(int(order_id), market_maker_response[order_id])


    # TODO: Check with Mohammed (and marketmakers/cow) what format the bids will be in.
    #  Does amount_in/amount_out flip when sell order bool is true/false? We need to DOUBLE CHECK
    # TODO: There is no check on amountOut. Add this (just to verify it's equal)
    def add_bid(self, order_id, new_bid):
        best_bid = self.best_bid[order_id]
        is_sell_order = self.is_sell_order[order_id]

        print("Comparing bid")
        if best_bid == {} \
        or (is_sell_order and int(new_bid.get("amountIn")) > int(best_bid.get("amountIn"))) \
        or (not is_sell_order and int(new_bid.get("amountIn")) < int(best_bid.get("amountIn"))):
            print("Updating best_bird for order " + str(order_id))
            self.best_bid[order_id] = new_bid

