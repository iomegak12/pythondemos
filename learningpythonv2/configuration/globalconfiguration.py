import os


class GlobalConfiguration:
    def get():
        configuration = {}
        customerServiceUrl = os.environ['CUSTOMER_SERVICE_URL']

        if(customerServiceUrl is None):
            raise Exception(
                'Invalid Customer Service URL Configuration Provided!')

        configuration['CUSTOMER_SERVICE_URL'] = customerServiceUrl

        return configuration
