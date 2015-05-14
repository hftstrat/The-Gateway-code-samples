from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface

ip, port = "localhost", 4000  # Connection details
contract, is_buy, qty = "XCME_Eq NQ (M15)", False, 1  # Order details

""" Connect and send order thru gateway """
socket_client = SocketClient(ip, port)
gateway = GatewayInterface(socket_client)
gateway.send_market_order(contract, is_buy, qty)
