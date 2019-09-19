import models

def as_customer_payload(dict):
    customer = models.Customer(
        dict['id'], dict['name'],
        dict['address'], dict['credit'],
        dict['status'], dict['remarks'])
    return customer