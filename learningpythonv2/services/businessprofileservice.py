import requests
import json
import models
import utilities
import configuration


class BusinessProfileService:
    def __init__(self):
        globalConfig = configuration.GlobalConfiguration.get()
        customerServiceUrl = globalConfig['CUSTOMER_SERVICE_URL']
        response = requests.get(customerServiceUrl)
        responseText = response.text
        self.businessProfiles = json.loads(
            responseText,
            object_hook=utilities.BusinessProfileEncoder.transform)

    def getBusinessProfiles(self):
        return self.businessProfiles
