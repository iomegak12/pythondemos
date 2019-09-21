class InternetOrder:
    def __init__(self, orderId, orderDate, productId, units):
        self.orderId, self.orderDate, self.productId, self.units = \
            orderId, orderDate, productId, units

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.orderId, self.orderDate, self.productId, self.units)
