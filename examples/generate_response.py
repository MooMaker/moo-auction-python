import json
import random


def generate_three_responses(filepath):
    market_makers = [
        ["0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
         "0xea2ba7a7a8fc1c0ef93aec9833fde9f8bd425ddec45090cdd0c86a1bc75dd0f825e2a3e978d46a18f5ea9a61c09d52849d547c0f41ca6fae7480835307352a241b"],
        ["0x8165049D60CAE302F0540134Dcf0939e0Fbf142f",
         "0xf86c0a8502540be400825208944bbeeb066ed09b7aed07bf39eee0460dfa261520880de0b6b3a7640000801ca0f3ae52c1ef3300f44df0bcfd1341c232ed613467"],
        ["0x11FFb891f7f40Af61FAeC19eB05C58a32d1b2D2D",
         "a0f3ae52c1ef3300f44df0bcfd1341c232ed6134672b16e35699ae3f5fe2493379a023d23d2955a239dd6f61c4e8b2678d174356ff424eac53da53e17706c43ef871"],
    ]
    for i in range(len(market_makers)):
        split_filepath = filepath.split("_input")
        generate_response(filepath, market_makers[i], split_filepath[0] + "_response" + str(i+1) + split_filepath[1])


def generate_response(filepath, market_maker, filename="sample.json"):
    response = {}
    cow_file = open(filepath)
    cow_json = json.load(cow_file)
    orders = cow_json["orders"]
    for order_id in orders:
        order = orders[order_id]
        if order["is_sell_order"]:
            tokenIn = order["sell_token"]
            tokenOut = order["buy_token"]
            amountIn = order["sell_amount"]
            amountOut = order["buy_amount"]
        else:
            tokenIn = order["buy_token"]
            tokenOut = order["sell_token"]
            amountIn = order["buy_amount"]
            amountOut = order["sell_amount"]
        validTo = 1628035200
        makerAddress = market_maker[0],
        makerSignature = market_maker[0]

        # Randomize amountInt a little bit
        amountIn = str(int(int(amountIn) * (100+random.randint(-5,5))/100))

        response[order_id] = {"tokenIn": tokenIn, "tokenOut": tokenOut, "amountIn": amountIn, "amountOut": amountOut,
                              "validTo": validTo, "makerAddress": makerAddress, "makerSignature": makerSignature }

    return write_file(response, filename)

def write_file(response_dict, filename="sample.json"):
    # Serializing json
    json_object = json.dumps(response_dict, indent=2)

    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)

generate_three_responses('../examples/same_pair_orders_shared_instances/same_pair_orders_instance2_input.json')