class InternetOrder:
    def __init__(self, orderId, orderDate, customerId, billingAddress,
                 shippingAddress, units, amount, remarks):
        self.orderId, self.orderDate, self.customerId, \
            self.billingAddress, self.shippingAddress, self.units, \
            self.amount, self.remarks = \
            orderId, orderDate, customerId, billingAddress, shippingAddress, \
            units, amount, remarks

    def toString(self):
        message = "{}, {}, {}, {}, {}, {}, {}, {}"

        return message.format(self.orderId, self.orderDate,
                              self.billingAddress, self.shippingAddress, self.units,
                              self.amount, self.remarks)
