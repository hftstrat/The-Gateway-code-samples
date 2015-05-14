import json
import socket_commands as scmd


class JsonSendData:

    def __init__(self):
        return

    def market_data_request(self, contract_id):
        data = dict()
        data[scmd.field_market_data_request] = True
        data[scmd.field_contract_id] = contract_id
        return json.dumps(data)

    def position_data_request(self):
        data = dict()
        data[scmd.field_position_data_request] = True
        return json.dumps(data)

    def accound_data_request(self):
        data = dict()
        data[scmd.field_account_data_request] = True
        return json.dumps(data)

    def order_data_request(self):
        data = dict()
        data[scmd.field_order_data_request] = True
        return json.dumps(data)

    def send_limit_order(self, contract_id, is_buy, price, qty):
        data = dict()
        data[scmd.field_send_limit_order] = True
        data[scmd.field_contract_id] = contract_id
        data[scmd.field_is_buy] = is_buy
        data[scmd.field_price] = price
        data[scmd.field_qty] = qty
        return json.dumps(data)

    def send_market_order(self, contract_id, is_buy, qty):
        data = dict()
        data[scmd.field_send_market_order] = True
        data[scmd.field_contract_id] = contract_id
        data[scmd.field_is_buy] = is_buy
        data[scmd.field_qty] = qty
        return json.dumps(data)