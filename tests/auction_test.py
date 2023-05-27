import pytest
import json
from auction import Auction

def test_single_order_single_response():
    cow_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    order_json = json.load(cow_file)
    auction = Auction(order_json)

    mm_file = open('../examples/mm_response_1.json')
    mm_order = json.load(mm_file)
    auction.parse_bids(mm_order)
    assert mm_order["0"] == auction.best_bid[0]

def test_single_order_multiple_response():
    cow_file = open('../examples/single_order_shared_instances/single_order_instance1_input.json')
    order_json = json.load(cow_file)
    auction = Auction(order_json)

    mm_file_paths = ['../examples/mm_response_1.json',
                '../examples/mm_response_2.json',
                '../examples/mm_response_3.json']
    mm_orders = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_orders.append(json.load(mm_file))
        auction.parse_bids(mm_orders[-1])
    assert mm_orders[1]["0"] == auction.best_bid[0]


def test_same_pair_orders_multiple_response():
    cow_file = open('../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_input.json')
    order_json = json.load(cow_file)
    auction = Auction(order_json)

    mm_file_paths = ['../examples/same_pair_orders_shared_instances/mm_response_1.json',
                '../examples/same_pair_orders_shared_instances/mm_response_2.json',
                '../examples/same_pair_orders_shared_instances/mm_response_3.json']
    mm_orders = []
    for mm_file_path in mm_file_paths:
        mm_file = open(mm_file_path)
        mm_orders.append(json.load(mm_file))
        auction.parse_bids(mm_orders[-1])
    assert mm_orders[2]["0"] == auction.best_bid[0]
    assert mm_orders[2]["1"] == auction.best_bid[1]
