__author__ = 'jamesma'

import datetime as dt


class MarketData:
    def __init__(self, data):
        self.timestamp = 0
        self.datetime = dt.datetime.now()
        self.market_id = None
        self.last_price = 0
        self.total_volume = 0
        self.tick_value = 0
        self.numerator = 1
        self.bids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.asks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bvols = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.avols = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.__parse_data(data)

    def __parse_data(self, data):
        self.numerator = data.get("Numerator")
        self.market_id = data.get("MarketId")
        self.tick_value = data.get("TickValue")
        self.total_volume = data.get("TotalVolume")
        self.timestamp = data.get("Timestamp")
        self.bids = data.get("Bids")
        self.bvols = data.get("BidVolumes")
        self.asks = data.get("Asks")
        self.avols = data.get("AskVolumes")
        self.last_price = data.get("LastPrice")

    def dt_from_timestamp(self):
        return dt.datetime(1, 1, 1) + dt.timedelta(microseconds=self.timestamp/10)

    def get_bid_price(self, rank):
        return self.bids[rank-1]

    def get_ask_price(self, rank):
        return self.asks[rank-1]

    def get_bid_volume(self, rank):
        return self.bvols[rank-1]

    def get_ask_volume(self, rank):
        return self.avols[rank-1]