import os

INVALID_CONFIGURATION = 'Invalid App. Configuration Provided!'


class GlobalConfiguration:
    def get():
        configuration = {}

        customerServiceUrl = os.environ['CUSTOMER_SERVICE_URL']
        mongoServer = os.environ['MONGO_SERVER']
        mongoPort = os.environ['MONGO_PORT']

        if customerServiceUrl is None:
            raise Exception(INVALID_CONFIGURATION)

        configuration['CUSTOMER_SERVICE_URL'] = customerServiceUrl
        configuration['MONGO_SERVER'] = mongoServer
        configuration['MONGO_PORT'] = mongoPort

        return configuration
