from prettytable import PrettyTable


class PrettyTableGenerator:
    def getTable(businessProfiles):
        if businessProfiles is None:
            raise Exception('Invalid Business Profiles Collection Specified!')

        table = PrettyTable(['Id', 'Name', 'City', 'Email', 'Phone'])

        for businessProfile in businessProfiles:
            table.add_row([
                businessProfile.id, businessProfile.fullName,
                businessProfile.city, businessProfile.email, businessProfile.phone])

        return table

    def getOrderTable(orders):
        if(orders is None):
            raise Exception('Invalid Orders Collection Specified!')

        table = PrettyTable(
            ['Order #', 'Order Date', 'Customer', 'Units', 'Amount'])

        for order in orders:
            table.add_row([
                order.orderId, order.orderDate, order.customerId,
                order.units, order.amount])

        return table
