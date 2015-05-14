from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface


def on_account_data(data):
    print data


def connect_and_stream_account_data(ip, port):
    try:
        socket_client = SocketClient(ip, port)
        gateway = GatewayInterface(socket_client)
        gateway.set_data_handlers(account_data=on_account_data)
        gateway.request_account_updates()
        socket_client.loop()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print e

    socket_client.shutdown()

if __name__ == "__main__":
    ip, port = "localhost", 4000
    connect_and_stream_account_data(ip, port)