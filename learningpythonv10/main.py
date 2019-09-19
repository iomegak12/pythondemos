import services
import models
import utilities

if __name__ == '__main__v1':
    fileName = './data/customers.json'
    customerService = services.CustomerService(fileName)
    customers = customerService.getCustomers()

    for customer in customers:
        print('{}, {}, {}'.format(
            customer.id, customer.name, customer.status))

    filteredCustomers = customerService.getCustomersByName('old')

    for filteredCustomer in filteredCustomers:
        print(filteredCustomer.name)

    peopleService = services.PeopleService()
    people = peopleService.getPeople()
    table = utilities.TableGenerator.getPrettyTable(people)

    print(table)

if __name__ == '__main__v2':
    import random
    import json

    class CustomContext:
        def __init__(self):
            self.data = random.randrange(1, 10000)

        def __enter__(self):
            return self.data

        def __exit__(self, execType, execValue, execTrace):
            return True

    with CustomContext() as context:
        print(context)

    with open('./data/customers.json', 'r') as file:
        data = json.load(file)

    print(data)

if __name__ == '__main__v3':
    peopleService = services.PeopleService()
    people = peopleService.getPeople()
    iterator = iter(people)

    while True:
        try:
            currentItem = next(iterator)
            print(currentItem.toString())
        except StopIteration as error:
            print('Iteration Completed!')
            break

if __name__ == '__main__v4':
    class Generator:
        def __init__(self, noOfTimes):
            self.times = noOfTimes

        def getData(self):
            data = range(self.times)

            for value in data:
                yield value

            print('Completed!')

    generatorObj = Generator(34)
    collection = generatorObj.getData()

    while True:
        try:
            print(next(collection))
        except StopIteration as error:
            break

if __name__ == '__main__v5':
    def getData():
        counter = 1

        def processAndGet():
            nonlocal counter
            counter += 1

            return counter

        return processAndGet

    o = getData()

    print(o())
    print(o())

if __name__ == '__main__v6':
    class Logger:
        def __init__(self, function):
            self.function = function

        def __call__(self, *args, **kargs):
            print('Started the work ...')
            self.function()
            print('Completed the Work!')

    @Logger
    def doWork():
        print('Doing the work!')

    doWork()

if __name__ == '__main__v7':
    from injector import Injector, inject

    class Inner:
        def __init__(self):
            self.value = 20

    class Outer:
        @inject
        def __init__(self, inner: Inner):
            if inner is None:
                raise Exception('Invalid Argument SpecifieD!')

            print(inner.value)

    di = Injector()
    outer = di.get(Outer)

if __name__ == '__main__v8':
    from pymongo import MongoClient
    import pprint

    client = MongoClient(host="localhost", port=27017)
    db = client.javatpoint
    employees = db.employees

    employee = {
        "id": "10001",
        "name": "Ramkumar",
        "reference": "Bangalore"
    }

    employees.insert_one(employee)

    pprint.pprint(employees.find_one())

if __name__ == '__main__v9':
    import unittest

    def add(val):
        return val * 2

    class Tests(unittest.TestCase):
        def test(self):
            input = 10
            expectedOutput = 76
            actualOutput = add(input)

            self.assertEqual(actualOutput, expectedOutput)

    unittest.main()

if __name__ == '__main__':
    import threading
    import time

    lock = threading.Lock()

    def thread_test(name, wait, value):
        while value:
            lock.acquire()
            time.sleep(wait)
            print("Lock Acquired ... Running {} {} \n ...".format(name, value))
            value -= 1
            lock.release()

    class DataLoader(threading.Thread):
        def __init__(self, id, name, wait):
            threading.Thread.__init__(self)
            self.id = id
            self.name = name
            self.wait = wait

        def run(self):
            thread_test(self.name, self.wait, 10)

    t1 = DataLoader(1, "Thread 1", 0.1)
    t2 = DataLoader(2, "Thread 2", 0.2)
    t3 = DataLoader(3, "Thread 3", 0.3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print('All threads have completed their work!')
