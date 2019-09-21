import json
import threading
import models
import utilities
from .baseservice import BaseService


class ProductService(threading.Thread, BaseService):
    def __init__(self, fileName):
        if fileName is None:
            raise Exception('Invalid Products File Name Specified!')

        self.__fileName = fileName
        threading.Thread.__init__(self)

    def run(self):
        try:
            fileHandle = open(self.__fileName, 'r')
            self.products = json.load(
                fileHandle,
                object_hook=utilities.ProductDecoder.transform)
        except Exception as error:
            print('Error Occurred, Details : {}'.format(str(error)))
        finally:
            fileHandle.close()

        if not(self.callback is None):
            self.callback(self.products)

    def getProductById(self, id):
        if id is None:
            raise Exception('Invalid Product Id Specified!')

        for product in self.products:
            if(product.productId == id):
                filteredProduct = product
                break

        return filteredProduct
