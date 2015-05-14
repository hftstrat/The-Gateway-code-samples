from classes.socket_client import SocketClient
import classes.gateway_interface as Gi

ip, port = "10.211.55.3", 4000  # Connection details
contract, price, is_buy, qty = "XCME_Eq NQ (M15)", 443350, False, 1  # Order details

socket_client = SocketClient(ip, port)
gateway = Gi.GatewayInterface(socket_client)
gateway.send_limit_order(contract, is_buy, price, qty)
