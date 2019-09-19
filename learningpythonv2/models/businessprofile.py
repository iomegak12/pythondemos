from .customerprofile import CustomerProfile


class BusinessProfile(CustomerProfile):
    def __init__(self, id, fullName, avatar, city, email, phone):
        super().__init__(id, fullName, avatar)

        self.city, self.email, self.phone = \
            city, email, phone

    def toString(self):
        return "{}, {}, {}, {}".format(
            super().toString(), self.city, self.email, self.phone)
