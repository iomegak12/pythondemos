import models


class ProductDecoder:
    def transform(dictionary):
        if(dictionary is None):
            raise Exception('Invalid Product Details Specified!')

        product = models.Product(
            dictionary['productId'], dictionary['title'],
            dictionary['qtyInStock'], dictionary['unitPrice'])

        return product
