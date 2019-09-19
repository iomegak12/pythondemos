from injector import inject
import services
import decorators

INVALID_CUSTOMER_SERVICE = 'Invalid Customer Service Specified!'
INVALID_ORDER_SERVICE = 'Invalid Order Service Specified!'
INVALID_CALLBACK = 'Invalid Callback Specified!'


class DataController:
    @inject
    def __init__(self, customerService: services.CustomerService,
                 orderService: services.OrderService):
        if customerService is None:
            raise Exception(INVALID_CUSTOMER_SERVICE)

        if orderService is None:
            raise Exception(INVALID_ORDER_SERVICE)

        self.__customerService = customerService
        self.__orderService = orderService

    @decorators.logger
    def process(self, callback):
        if callback is None:
            raise Exception(INVALID_CALLBACK)

        self.__customerService.start()
        self.__orderService.start()

        self.__customerService.join()
        self.__orderService.join()

        callback()
