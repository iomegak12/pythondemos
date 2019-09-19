class CustomerProfile:
    def __init__(self, id, fullName, avatar):
        self.id, self.fullName, self.avatar = \
            id, fullName, avatar

    def toString(self):
        return "{}, {}, {}".format(
            self.id, self.fullName, self.avatar)
