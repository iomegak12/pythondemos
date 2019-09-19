class Person:
    def __init__(self, id, name, city, avatar):
        self.id, self.name, self.city, self.avatar = \
            id, name, city, avatar

    def toString(self):
        return "{}, {}, {}, {}".format(
            self.id, self.name, self.city, self.avatar)
