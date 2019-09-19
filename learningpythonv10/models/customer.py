class Customer:
    def __init__(self, id, name, address, credit, status, remarks):
        self.id = id
        self.name = name
        self.address = address
        self.credit = credit
        self.status = status
        self.remarks = remarks

    def toString(self):
        message = "{}, {}, {}, {}, {}, {}"
        return message.format(self.id, self.name, self.address, \
                              self.credit, self.status, self.remarks)
