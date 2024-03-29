import json
import models
import utilities
import threading
from .baseservice import BaseService


class InternetOrderService(threading.Thread, BaseService):
    def __init__(self, fileName):

        if fileName is None:
            raise Exception('Invalid Orders File Name Specified!')

        self.__fileName = fileName

        threading.Thread.__init__(self)

    def run(self):
        with open(self.__fileName, 'r') as fileHandle:
            self.orders = json.load(
                fileHandle, object_hook=utilities.InternetOrderDecoder.transform)

        if not (self.callback is None):
            self.callback(self.orders)
