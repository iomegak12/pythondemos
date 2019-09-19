from injector import Injector, inject
import controllers
import utilities
import services

if __name__ == '__main__':
    def configure(binder):
        binder.bind(services.CustomerService,
                    to=services.CustomerService(
                        lambda customers:
                            print(utilities.PrettyTableGenerator.getTable(customers))
                    ))

        binder.bind(services.OrderService,
                    to=services.OrderService(
                        lambda orders:
                            print(
                                utilities.PrettyTableGenerator.getOrderTable(orders))
                    ))

    injectorObj = Injector([configure])
    controller = injectorObj.get(controllers.DataController)

    def process():
        controller.process(
            lambda: print('Both Results have been processed!')
        )

    process()

    print('End of the World!')
