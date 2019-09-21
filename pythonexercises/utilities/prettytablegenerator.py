from prettytable import PrettyTable
import models


class PrettyTableGenerator:
    def getProcessedOrdersTable(processedOrders):
        if processedOrders is None:
            raise Exception('Invalid Processed Orders Specified!')

        table = PrettyTable(
            ['orderId', 'orderDate', 'productId', 'units', 'amount', 'status'])

        for processedOrder in processedOrders:
            table.add_row(
                [
                    processedOrder.orderId, processedOrder.orderDate,
                    processedOrder.productId, processedOrder.units,
                    processedOrder.amount, processedOrder.status
                ])

        return table
