class AccountData:
    def __init__(self, data):
        self.firm = None
        self.unrealized_pnl = 0
        self.description = ""
        self.account_number = None
        self.timestamp = None
        self.commissions = 0
        self.realized_pnl = 0
        self.total_pnl = 0
        self.balance = 0
        self.available_cash = 0
        self.account_id = None

        self.__parse_data(data)

    def __parse_data(self, data):
        self.firm = data.get("Firm")
        self.unrealized_pnl = data.get("UPnL")
        self.description = data.get("Description")
        self.account_number = data.get("AccountNumber")
        self.timestamp = data.get("Timestamp")
        self.commissions = data.get("FeesAndCommissions")
        self.total_pnl = data.get("PnL")
        self.balance = data.get("Balance")
        self.realized_pnl = data.get("RPnL")
        self.available_cash = data.get("AvailableCash")
        self.account_id = data.get("AccountId")