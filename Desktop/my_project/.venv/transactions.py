class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: PredictionResult):
        self.transactions.append(transaction)

    def get_transactions_by_violation_type(self, violation_type: str) -> list[PredictionResult]:
        return [t for t in self.transactions if t.get_violation_type() == violation_type]

    def get_transactions_by_response_status(self, response_status: str) -> list[PredictionResult]:
        return [t for t in self.transactions if t.get_response_status() == response_status]