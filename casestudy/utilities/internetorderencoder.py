import models

INVALID_ARGUMENTS = 'Invalid Order Profile Argument(s) Specified!'


class InternetOrderEncoder:
    def transform(dictionary):
        if dictionary is None:
            raise Exception(INVALID_ARGUMENTS)

        internetOrder = models.InternetOrder(
            dictionary['orderId'], dictionary['orderDate'],
            dictionary['customerId'], dictionary['billingAddress'],
            dictionary['shippingAddress'], dictionary['units'],
            dictionary['amount'], dictionary['remarks'])

        return internetOrder
