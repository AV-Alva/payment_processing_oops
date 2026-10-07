from payment import (
    CreditCardPayment,
    UPIPayment,
    NetBankingPayment
)

from payment.exceptions import InvalidPaymentAmountError
from payment.logger_config import logger


def process_payment(payment_method, amount):
    """Process payment using any Payment object."""

    try:
        payment_method.pay(amount)

    except InvalidPaymentAmountError as error:
        print("Payment Failed:", error)
        logger.error("Payment failed: %s", error)

    except Exception as error:
        print("Unexpected Error:", error)
        logger.exception("Unexpected payment error")


def main():

    print("\n===== PAYMENT PROCESSING SYSTEM =====")

    payments = [
        CreditCardPayment(),
        UPIPayment(),
        NetBankingPayment()
    ]

    amounts = [2500, 1200, 5000]

    for payment_method, amount in zip(payments, amounts):
        process_payment(payment_method, amount)

    print("\n===== PAYMENT PROCESSING COMPLETED =====")


if __name__ == "__main__":
    main()