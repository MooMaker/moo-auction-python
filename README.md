# MooMaker Offchain Services

This repository contains the offchain services that MooMaker uses to connect the COW solver with marketmakers via the MooMaker auction system.

The offchain services consists of 2 parts:
- REST API with a single POST endpoint, which the solver accesses to publish a new COW batch auction.
- A websocket which:
  - Publishes the COW batch auction to the market makers.
  - Receives bids from market makers.
  - Informs market makers when a bid has been accepted.

## Usage

Running main.py will start the websocket and REST API on 2 different servers.
- REST API: http://127.0.0.1:5000/cow
- websocket: [ws://localhost:8765/](ws://localhost:8765/)

Use the files in the examples directory to test the flow as follows:
1. Open the websocket connection
2. Send the `single_order_instance1_input.json` in the body (as json) with a POST request to the REST endpoint. A copy of this file should now appear on the websocket.
3. Within 5 seconds, send the content of `market_maker-response.json` via the websocket.
4. The auction is closed and the winning bid is announced [NOT IMPLEMENTED YET]