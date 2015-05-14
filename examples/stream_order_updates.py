from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface


def on_unhandled_server_data(data):
    print "on_generic_server_command(): ", data


def on_account_data(data):
    print data


def on_order_data(data):
    print data


def connect_and_stream_order_data(ip, port):
    try:
        socket_client = SocketClient(ip, port)
        gateway = GatewayInterface(socket_client)
        gateway.set_data_handlers(unhandled_data=on_unhandled_server_data,
                                  account_data=on_account_data,
                                  order_data=on_order_data)
        gateway.request_order_updates()
        socket_client.loop()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print e

    socket_client.shutdown()

if __name__ == "__main__":
    ip, port = "10.211.55.3", 4000
    connect_and_stream_order_data(ip, port)