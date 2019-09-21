import os


class GlobalConfiguration:
    def get():
        productFileName = os.environ['PRODUCTS_FILE']
        orderFileName = os.environ['ORDERS_FILE']

        configuration = {}
        configuration['PRODUCTS_FILE'] = productFileName
        configuration['ORDERS_FILE'] = orderFileName

        return configuration
