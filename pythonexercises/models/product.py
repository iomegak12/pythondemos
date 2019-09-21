class Product:
    def __init__(self, productId, title, qtyInStock, unitPrice):
        self.productId, self.title, self.qtyInStock, self.unitPrice = \
            productId, title, qtyInStock, unitPrice

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.productId, self.title, self.qtyInStock, self.unitPrice)
