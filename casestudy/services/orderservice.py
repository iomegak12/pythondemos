from pymongo import MongoClient

import threading
import config
import utilities
import models

INVALID_CALLBACK = 'Invalid Order Service Callback Specified!'
INVALID_MONGO_SERVER = 'Invalid Mongo server Configuration Specified!'
INVALID_MONGO_PORT = 'Invalid Mongo Server Port Configuration Specified!'

MONGO_DB = 'ordersystemdb'
MONGO_COLLECTION = 'internetorders'

class OrderService(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)

        if callback is None:
            raise Exception(INVALID_CALLBACK)

        self.__callback = callback

        globalConfigObj = config.GlobalConfiguration.get()
        mongoServer = globalConfigObj['MONGO_SERVER']

        if mongoServer is None:
            raise Exception(INVALID_MONGO_SERVER)

        self.__mongoServer = mongoServer

        mongoPort = globalConfigObj['MONGO_PORT']

        if mongoPort is None:
            raise Exception(INVALID_MONGO_PORT)

        self.__mongoPort = mongoPort

    def run(self):
        client = MongoClient(
            host=self.__mongoServer, port=int(self.__mongoPort))
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        orders = collection.find({})

        internetOrders = []

        for order in orders:
            internetOrders.append(
                utilities.InternetOrderEncoder.transform(order))

        if not(self.__callback is None):
            self.__callback(internetOrders)
