class CustomerProfile:
    def __init__(self, id, fullName, avatar, city, email, phone):
        self.id, self.fullName, self.avatar, self.city, self.email, self.phone = \
            id, fullName, avatar, city, email, phone

    def toString(self):
        return "{}, {}, {}, {}, {}, {}".format(
            self.id, self.fullName, self.avatar,
            self.city, self.email, self.phone)
