from payments import PaymentStrategy

class PaypalPaymentService(PaymentStrategy):
    def processPayment(self, amount: float):
        print(f"Payment completed using Paypal. Amount: {amount}")

