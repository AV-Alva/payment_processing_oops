from .payment import Payment
from .exceptions import InvalidPaymentAmountError
from .logger_config import logger

class UPIPayment(Payment):

    def pay(self, amount):

        if amount <= 0:
            raise InvalidPaymentAmountError(
                "Payment amount must be greater than zero."
            )

        print(f"₹{amount:.2f} paid using UPI.")

        logger.info(
            "UPI payment successful: ₹%.2f",
            amount
        )