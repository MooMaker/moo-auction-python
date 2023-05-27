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
    mm_order = json.load(mm_file)
    auction.parse_bids(mm_order)
    assert mm_order["0"] == auction.best_bid[0]

def test_single_order_multiple_response():
    auction_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/single_order_shared_instances/single_order_instance1_response1.json',
                '../examples/single_order_shared_instances/single_order_instance1_response2.json',
                '../examples/single_order_shared_instances/single_order_instance1_response3.json']
    mm_orders = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_orders.append(json.load(mm_file))
        auction.parse_bids(mm_orders[-1])
    assert mm_orders[1]["0"] == auction.best_bid[0]


def test_same_pair_orders_multiple_response():
    auction_file = open('../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response1.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response2.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_response3.json']
    mm_orders = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_orders.append(json.load(mm_file))
        auction.parse_bids(mm_orders[-1])
    assert mm_orders[2]["0"] == auction.best_bid[0]
    assert mm_orders[1]["1"] == auction.best_bid[1]

def test_same_pair_orders_multiple_response_generated():
    auction_file = open('../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_input.json')
    auction_json = json.load(auction_file)
    auction = Auction(auction_json)

    mm_file_paths = ['../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response1.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response2.json',
                '../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_response3.json']
    mm_orders = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_orders.append(json.load(mm_file))
        auction.parse_bids(mm_orders[-1])
    assert mm_orders[1]["0"] == auction.best_bid[0]
    assert mm_orders[0]["1"] == auction.best_bid[1]
