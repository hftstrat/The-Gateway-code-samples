class OrderData:
    def __init__(self, data):
        self.order_type = None
        self.order_id = None
        self.price = None
        self.qty = None
        self.filled_qty = None
        self.tradable_id = None
        self.is_buy = True
        self.order_state = None
        self.order_time = None
        self.timestamp = None
        self.update_time = None

        self.__parse_data(data)

    def __parse_data(self, data):
        self.order_id = data.get("OrderId")
        self.order_type = data.get("OrderType")
        self.limit_price = data.get("Price")
        self.qty = data.get("Qty")
        self.filled_qty = data.get("FilledQty")
        self.tradable_id = data.get("TradableId")
        self.is_buy = data.get("IsBuy")
        self.timestamp = data.get("Timestamp")
        self.order_state = data.get("OrderState")
        self.order_time = data.get("OrderTime")
        self.update_time = data.get("UpdateTime")

    def is_filled_completely(self):
        return self.filled_qty == self.qty
