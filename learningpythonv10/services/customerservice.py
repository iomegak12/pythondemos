import json
import models
import utilities
import re

class CustomerService:
    def __init__(self, fileName):
        self.__fileName = fileName

        try:
            file = open(self.__fileName, 'r')
            self.customers = json.load(
                file, object_hook=utilities.as_customer_payload)
        except Exception as error:
            print('Error Occurred ... ' + str(error))
        finally:
            file.close()

    def getCustomers(self): return self.customers

    def getCustomersByName(self, name):
        filteredCustomers = filter(
            lambda customer: re.search(name, customer.name, re.IGNORECASE), self.customers)
        return filteredCustomers
