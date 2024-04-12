from payments import PaymentStrategy

class DebitCardPaymentService(PaymentStrategy):
    def processPayment(self, amount: float):
        print(f"Payment completed using Debit Card. Amount: {amount}")

