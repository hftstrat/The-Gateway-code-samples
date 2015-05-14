from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface

ip, port = "localhost", 4000  # Connection details
contract, price, is_buy, qty = "XCME_Eq NQ (M15)", 443350, False, 1  # Order details

socket_client = SocketClient(ip, port)
gateway = GatewayInterface(socket_client)
gateway.send_limit_order(contract, is_buy, price, qty)
