import requests
import json
import threading
import time

import models
import utilities
import config

INVALID_CALLBACK = 'Invalid Customer Service Callback Specified!'


class CustomerService(threading.Thread):
    def __init__(self, callback):
        if callback is None:
            raise Exception(INVALID_CALLBACK)

        threading.Thread.__init__(self)
        self.__callback = callback
        globalConfig = config.GlobalConfiguration.get()
        self.__customerServiceUrl = globalConfig['CUSTOMER_SERVICE_URL']

    def run(self):
        if not(self.__customerServiceUrl is None):
            response = requests.get(self.__customerServiceUrl)
            responseText = response.text
            customerProfiles = json.loads(
                responseText, object_hook=utilities.BusinessProfileEncoder.transform)

            if not(self.__callback is None):
                self.__callback(customerProfiles)
