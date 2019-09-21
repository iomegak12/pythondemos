import models


class InternetOrderDecoder:
    def transform(dictionary):
        if dictionary is None:
            raise Exception('Invalid Order Details Specified!')

        order = models.InternetOrder(
            dictionary['orderId'], dictionary['orderDate'],
            dictionary['productId'], dictionary['units'])

        return order
