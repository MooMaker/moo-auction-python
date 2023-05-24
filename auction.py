class Auction:

    def __init__(self, json):
        self.json = json
        self.id = json["auction_id"]
        self.end_time = json["end_time"]
        self.is_sell_order = True #TODO: Make logic for this
        # TODO: we now assume it's 1 order per auction but this is not the case
        #  create list of bids corresponding to order id's
        self.best_bid = {}
        for order_id in json["orders"]:
            self.best_bid[int(order_id)] = {}

    # TODO: Check with Mohammed (and marketmakers/cow) what format the bids will be in.
    #  Does amount_in/amount_out flip when sell order bool is true/false? We need to DOUBLE CHECK
    def addBid(self, order_id, new_bid):
        # TODO: Also here we need to match it to order_id
        print("Adding bid")
        if self.best_bid[order_id] == {} \
        or (self.is_sell_order and new_bid.get("amountIn") > self.best_bid.get("amountIn")) \
        or (not self.is_sell_order and new_bid.get("amountIn") < self.best_bid.get("amountIn")):
            self.best_bid[order_id] = new_bid

