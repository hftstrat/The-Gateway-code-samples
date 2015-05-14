"""
Stream all positions data.
"""

from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface


def on_position_data(data):
    print data


def connect_and_stream_position_data(ip, port):
    try:
        socket_client = SocketClient(ip, port)
        gateway = GatewayInterface(socket_client)
        gateway.set_data_handlers(position_data=on_position_data)
        gateway.request_position_updates()
        socket_client.loop()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print e

    socket_client.shutdown()

if __name__ == "__main__":
    ip, port = "localhost", 4000
    connect_and_stream_position_data(ip, port)