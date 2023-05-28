import json

from auction import Auction


def create_auction():
    auction_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)


def test_single_order_single_response():
    auction_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file = open('../examples/single_order_shared_instances/single_order_instance1_response1.json')
    mm_json = json.load(mm_file)
    mm_bids = mm_json["bids"]
    auction.parse_bids(mm_bids)
    assert mm_bids["0"] == auction.best_bid[0]

def test_single_order_multiple_response():
    auction_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/single_order_shared_instances/single_order_instance1_response1.json',
                '../examples/single_order_shared_instances/single_order_instance1_response2.json',
                '../examples/single_order_shared_instances/single_order_instance1_response3.json']
    mm_bids = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_json = json.load(mm_file)
        mm_bids.append(mm_json["bids"])
        auction.parse_bids(mm_bids[-1])
    assert mm_bids[0]["0"] == auction.best_bid[0]


def test_same_pair_orders_multiple_response():
    auction_file = open('../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response1.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response2.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response3.json']
    mm_bids = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_json = json.load(mm_file)
        mm_bids.append(mm_json["bids"])
        auction.parse_bids(mm_bids[-1])
    assert mm_bids[2]["0"] == auction.best_bid[0]
    assert mm_bids[1]["1"] == auction.best_bid[1]

def test_same_pair_orders_multiple_response_generated():
    auction_file = open('../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response1.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response2.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response3.json']
    mm_bids = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_json = json.load(mm_file)
        mm_bids.append(mm_json["bids"])
        auction.parse_bids(mm_bids[-1])
    assert mm_bids[1]["0"] == auction.best_bid[0]
    assert mm_bids[1]["1"] == auction.best_bid[1]
