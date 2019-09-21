from injector import Injector
import utilities
import models
import config
import services
import controllers

if __name__ == '__main__':
    def configureBinding(binder):
        configObj = config.GlobalConfiguration.get()

        productsFileName = configObj['PRODUCTS_FILE']
        ordersFileName = configObj['ORDERS_FILE']

        binder.bind(services.ProductService,
                    to=services.ProductService(productsFileName))
        binder.bind(services.InternetOrderService,
                    to=services.InternetOrderService(ordersFileName))

    injector = Injector([configureBinding])
    processor = injector.get(controllers.DataProcessor)
    processedOrders = processor.process()
    processedOrdersTable = utilities.PrettyTableGenerator.getProcessedOrdersTable(
        processedOrders)

    print(processedOrdersTable)
