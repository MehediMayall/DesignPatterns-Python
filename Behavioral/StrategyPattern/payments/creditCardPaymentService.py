from payments import PaymentStrategy

class CreditCardPaymentService(PaymentStrategy):
    def processPayment(self, amount: float):
        print(f"Payment completed using Credit Card. Amount: {amount}")

