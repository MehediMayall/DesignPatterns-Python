from payments import PaymentStrategy, PaymentService, CreditCardPaymentService, DebitCardPaymentService, PaypalPaymentService


if __name__ == "__main__":
    payment = PaymentService()
    payment.makePayment(PaypalPaymentService(),1000.50)