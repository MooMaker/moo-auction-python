class Auction:

    def __init__(self, json):
        self.json = json
        self.id = json["metadata"]["auction_id"]
        self.orders = json["orders"]
        # self.end_time = json["end_time"]
        # TODO: add end_time
        self.is_sell_order = {}
        self.best_bid = {}
        for order_id in self.orders:
            self.is_sell_order[int(order_id)] = self.orders[order_id]["is_sell_order"];
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
            # if self.validate_bid(order_id, new_bid):
            print("Updating best_bird for order " + str(order_id))
            self.best_bid[order_id] = new_bid

    def validate_bid(self, order_id, bid) -> bool:
        # TODO: What should we do if there is 1 invalid bid in a MM response? Do we still parse the remaining bids of this response?
        print("validating bid")
        order = self.orders[str(order_id)]
        if (self.is_sell_order[order_id]):
            amountOut = order["buy_amount"]
            tokenIn = order["sell_token"]
            tokenOut = order["buy_token"]
        else:
            amountOut = order["sell_amount"]
            tokenIn = order["buy_token"]
            tokenOut = order["sell_token"]

        if amountOut != bid["amountOut"]:
            print("Validation failed on amountOut for order_id: " + str(order_id))
            return False
        elif tokenIn != bid["tokenIn"]:
            print("Validation failed on tokenIn for order_id: " + str(order_id))
            return False
        elif tokenOut != bid["tokenOut"]:
            print("Validation failed on tokenOut for order_id: " + str(order_id))
            return False

        return True

