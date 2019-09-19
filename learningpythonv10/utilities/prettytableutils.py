import models
from prettytable import PrettyTable


class TableGenerator:
    def getPrettyTable(customers):
        table = PrettyTable(['id', 'name', 'city', 'avatar'])

        for customer in customers:
            table.add_row([customer.id, customer.name,
                           customer.city, customer.avatar])

        return table
