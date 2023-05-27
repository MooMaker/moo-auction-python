import json

def generate_response(filepath):
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
        makerAddress = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
        makerSignature = "0xea2ba7a7a8fc1c0ef93aec9833fde9f8bd425ddec45090cdd0c86a1bc75dd0f825e2a3e978d46a18f5ea9a61c09d52849d547c0f41ca6fae7480835307352a241b"
        # TODO: randomize maker details

        response[order_id] = {"tokenIn": tokenIn, "tokenOut": tokenOut, "amountIn": amountIn, "amountOut": amountOut,
                              "validTo": validTo, "makerAddress": makerAddress, "makerSignature": makerSignature }

    return write_file(response)

def write_file(response_dict):
    # Serializing json
    json_object = json.dumps(response_dict)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

generate_response('../examples/same_pair_orders_shared_instances/same_pair_orders_instance1_input.json')