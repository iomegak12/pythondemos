import os
import models
import json
import requests


def as_person_payload(dict):
    return models.Person(
        dict['id'], dict['name'],
        dict['city'], dict['avatar'])


class PeopleService:
    def __init__(self):
        try:
            url = os.environ['CUSTOMER_SERVICE_URL']
            response = requests.get(url)
            responseJson = response.text
            self.people = json.loads(
                responseJson, object_hook=as_person_payload)
        except Exception as error:
            print('Error Occurred, Details : {}'.format(str(error)))
        finally:
            print('Data Loaded!')

    def getPeople(self): return self.people
