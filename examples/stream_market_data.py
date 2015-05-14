"""
Stream market data for a single contract.
"""

from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface


def on_market_data(market_data):
    print market_data


def connect_and_stream_market_data(ip, port, contracts):
    try:
        socket_client = SocketClient(ip, port)
        gateway = GatewayInterface(socket_client)
        gateway.set_data_handlers(market_data=on_market_data)

        for contract in contracts:
            gateway.request_market_data(contract)

        socket_client.loop()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print e

    socket_client.shutdown()

if __name__ == "__main__":
    ip, port = "10.211.55.3", 4000
    #contracts = ["XCME_E YM (M15)"]  # Ensure contract is a valid exchange tradable month/year.
    #contracts = ["XCME_Eq NQ (M15)"]
    contracts = ["XCME_Eq ES (M15)"]
    connect_and_stream_market_data(ip, port, contracts)