import hashlib
import json
import random
import secrets
import string

from coincurve import PublicKey


def generate_maker_address():
    private_key = hashlib.sha256(secrets.token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = hashlib.sha256(public_key).digest()[-20:]
    return "0x" + addr.hex()

def generate_fake_signature():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=132))

def generate_multiple_responses(filepath, number_of_responses):
    for i in range(number_of_responses):
        split_filepath = filepath.split("_input")
        generate_response(filepath, generate_maker_address(), split_filepath[0] + "_response" + str(i+1) + split_filepath[1])


def generate_response(filepath, maker_address=generate_maker_address(), filename="sample.json"):
    cow_file = open(filepath)
    cow_json = json.load(cow_file)
    response = {"metadata": {"auction_id": cow_json["metadata"]["auction_id"]}, "bids": {}}
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

        # Randomize amountInt a little bit
        amountIn = str(int(int(amountIn) * (100+random.randint(-5,5))/100))

        response["bids"][order_id] = {"tokenIn": tokenIn, "tokenOut": tokenOut, "amountIn": amountIn, "amountOut": amountOut,
                              "validTo": validTo, "makerAddress": maker_address, "makerSignature": generate_fake_signature()}

    return write_file(response, filename)

def write_file(response_dict, filename="sample.json"):
    # Serializing json
    json_object = json.dumps(response_dict, indent=2)

    # Writing to sample.json
    with open(filename, "w") as outfile:
        outfile.write(json_object)


# # Use this to generate responses for given inputs. Outputs are placed in same directory as input file.
# generate_multiple_responses('../examples/single_order_shared_instances/single_order_instance1_input.json',3)
# generate_multiple_responses('../examples/single_order_shared_instances/single_order_instance2_input.json',3)