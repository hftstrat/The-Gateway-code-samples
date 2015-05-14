__author__ = 'jamesma'

class PositionData:
    def __init__(self, data):
        self.working_sells = 0
        self.timestamp = 0
        self.tradable_id = None
        self.working_buys = 0
        self.realized_pnl = 0
        self.unrealized_pnl = 0
        self.market_id = None
        self.avg_buy_price = 0
        self.last_updated = None
        self.buys = 0
        self.sells = 0
        self.net = 0
        self.avg_sell_price = 0

        self.__parse_data(data)

    def __parse_data(self, data):
        print data
        self.working_sells = data.get("WorkingSells")
        self.timestamp = data.get("Timestamp")
        self.tradable_id = data.get("TradableId")
        self.working_buys = data.get("WorkingBuys")
        self.realized_pnl = data.get("RealizedPnl")
        self.unrealized_pnl = data.get("UnrealizedPnl")
        self.market_id = data.get("MarketId")
        self.avg_buy_price = data.get("AverageBuyPrice")
        self.last_updated = data.get("LastUpdated")
        self.buys = data.get("Buys")
        self.sells = data.get("Sells")
        self.net = data.get("Net")
        self.avg_sell_price = data.get("AverageSellPrice")