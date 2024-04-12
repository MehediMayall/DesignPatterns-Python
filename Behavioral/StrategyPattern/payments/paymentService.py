from payments import PaymentStrategy


class PaymentService:
    def __init__(self):
        pass

    def makePayment(self, Payment: PaymentStrategy, Amount: float):
        Payment.processPayment(Amount)