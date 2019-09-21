from .product import Product
from .internetorder import InternetOrder


class ProcessedOrder:
    def __init__(self, productId, title, qtyInStock, unitPrice,
                 orderId, orderDate, units, amount, status):
        self.orderId, self.orderDate, self.productId, \
            self.title, self.qtyInStock, self.units, self.unitPrice, \
            self.amount, self.status = orderId, orderDate, productId, \
            title, qtyInStock, units, unitPrice, amount, status

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(
            self.orderId, self.orderDate, self.productId, self.title,
            self.qtyInStock, self.unitPrice, self.units,
            self.amount, self.status)
