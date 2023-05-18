

class Auction:

    def __init__(self, json, id, end_time):
        self.json = json
        self.id = id
        self.end_time = end_time
        self.is_sell_order = True #TODO: Make logic for this
        self.best_bid = {}

    # TODO: Check with Mohammed (and marketmakers/cow) what format the bids will be in.
    #  Does amount_in/amount_out flip when sell order bool is true/false? We need to DOUBLE CHECK
    def addBid(self, new_bid):
        print("Adding bid")
        self.best_bid = new_bid
        # if self.best_bid == {} \
        # or (self.is_sell_order and new_bid["amount_in"] > self.best_bid["amount_in"]) \
        # or (not self.is_sell_order and new_bid["amount_in"] < self.best_bid["amount_in"]):
        #     self.best_bid = new_bid

