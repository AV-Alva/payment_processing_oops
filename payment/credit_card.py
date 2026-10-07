from .payment import Payment
from .exceptions import InvalidPaymentAmountError
from .logger_config import logger


class CreditCardPayment(Payment):

    def pay(self, amount):

        if amount <= 0:
            raise InvalidPaymentAmountError(
                "Payment amount must be greater than zero."
            )

        print(f"₹{amount:.2f} paid using Credit Card.")

        logger.info(
            "Credit Card payment successful: ₹%.2f",
            amount
        )