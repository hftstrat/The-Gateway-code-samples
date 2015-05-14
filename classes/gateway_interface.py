import socket_commands as commands
import json
from json_send_data import JsonSendData
from market_data import MarketData
from position_data import PositionData
from order_data import OrderData
from account_data import AccountData


class GatewayInterface:

    def __init__(self, socket_client):
        self.__jsd = JsonSendData()
        self.__client = socket_client

        if self.__client is not None:
            self.__client.set_data_handler(self.__on_data_received)

        self.__on_unhandled_data = None
        self.__on_market_data_handler = None
        self.__on_order_handler = None
        self.__on_position_data_handler = None
        self.__on_account_data_handler = None

        self.data_buffer = ""

    def request_market_data(self, contract_id):
        self.__send_command_w_params(self.__jsd.market_data_request,
                                     contract_id)

    def request_position_updates(self):
        self.__send_command_w_params(self.__jsd.position_data_request)

    def request_account_updates(self):
        self.__send_command_w_params(self.__jsd.accound_data_request)

    def request_order_updates(self):
        self.__send_command_w_params(self.__jsd.order_data_request)

    def send_market_order(self, contract_id, is_buy, qty):
        self.__send_command_w_params(self.__jsd.send_market_order,
                                     contract_id, is_buy, qty)

    def send_limit_order(self, contract_id, is_buy, price, qty):
        self.__send_command_w_params(self.__jsd.send_limit_order,
                                     contract_id, is_buy, price, qty)

    def __send_command_w_params(self, func, *args):
        command = func(*args)
        command += commands.eol
        self.__client.__write_buffer_n_send__(command)
    """
    def modify_limit_order(self, order_id, qty, price):
        buff = str(commands.modify_limit_order_command) + commands.delimiter
        buff += order_id + commands.delimiter
        buff += str(qty) + commands.delimiter
        buff += str(price) + commands.delimiter
        buff += commands.eol
        self.__client.append_to_buffer(buff)

    def pull_order(self, order_id):
        buff = str(commands.pull_order_command) + commands.delimiter
        buff += order_id + commands.delimiter
        buff += commands.eol
        self.__client.append_to_buffer(buff)
    """
    def set_data_handlers(self, **kwargs):
        self.__on_unhandled_data = kwargs.get('unhandled_data')
        self.__on_market_data_handler = kwargs.get('market_data')
        self.__on_order_handler = kwargs.get('order_data')
        self.__on_position_data_handler = kwargs.get('position_data')
        self.__on_account_data_handler = kwargs.get('account_data')

    def __on_data_received(self, data):
        self.data_buffer += data
        self.data_buffer = self.__process_data_buffer(self.data_buffer)

    @staticmethod
    def __find_first_index(haystack, match):
        return haystack.find(match)

    def __process_data_buffer(self, data):
        eol_index = self.__find_first_index(data, commands.eol)
        while eol_index > 0:
            command = data[:eol_index]
            self.__process_command(command)
            data = data[(eol_index + len(commands.eol)):]
            eol_index = self.__find_first_index(data, commands.eol)
        return data

    def __process_command(self, raw_data):
        json_data = json.loads(raw_data)

        if self.__is_market_data(json_data):
            if self.__on_market_data_handler is not None:
                market_data = MarketData(json_data)
                self.__on_market_data_handler(market_data)
            return

        if self.__is_position_data(json_data):
            if self.__on_position_data_handler is not None:
                position_data = PositionData(json_data)
                self.__on_position_data_handler(position_data)
            return

        if self.__is_order_data(json_data):
            if self.__on_order_handler is not None:
                order_data = OrderData(json_data)
                self.__on_order_handler(order_data)
            return

        if self.__is_account_data(json_data):
            if self.__on_account_data_handler is not None:
                account_data = AccountData(json_data)
                self.__on_account_data_handler(account_data)
            return

        print "unhandled data from server:", raw_data
        if self.__on_account_data_handler is not None:
            self.__on_account_data_handler(json_data)

    @staticmethod
    def __is_market_data(data):
        return data is not None and commands.field_data_command in data and \
            data.get(commands.field_data_command) == commands.field_market_data_request

    @staticmethod
    def __is_position_data(data):
        return data is not None and commands.field_data_command in data and \
            data.get(commands.field_data_command) == commands.field_position_data_request

    @staticmethod
    def __is_order_data(data):
        return data is not None and commands.field_data_command in data and \
            data.get(commands.field_data_command) == commands.field_order_data_request

    @staticmethod
    def __is_account_data(data):
        return data is not None and commands.field_data_command in data and \
            data.get(commands.field_data_command) == commands.field_account_data_request