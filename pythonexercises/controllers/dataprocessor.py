from injector import inject
import services
import models


class DataProcessor:
    @inject
    def __init__(self, productService: services.ProductService,
                 ordersService: services.InternetOrderService):
        if productService is None:
            raise Exception('Invalid Product Service Specified!')

        if(ordersService is None):
            raise Exception('Invalid Orders Service Specified!')

        self.__productService = productService
        self.__ordersService = ordersService

    def process(self):
        def setProducts(products):
            self.__products = products

        def setOrders(orders):
            self.__orders = orders

        self.__productService.setCallback(setProducts)
        self.__ordersService.setCallback(setOrders)

        self.__productService.start()
        self.__ordersService.start()

        self.__productService.join()
        self.__ordersService.join()

        processedOrders = []

        for order in self.__orders:
            product = self.__productService.getProductById(order.productId)
            status = 'INVALID'

            if not(product is None):
                amount = product.unitPrice * order.units

                if(product.qtyInStock >= order.units):
                    status = 'PROCESSED'
                else:
                    status = 'STOCK UNAVAILABLE'

            processedOrder = models.ProcessedOrder(
                product.productId, product.title, product.qtyInStock, product.unitPrice,
                order.orderId, order.orderDate, order.units, amount, status)

            processedOrders.append(processedOrder)

        return processedOrders
