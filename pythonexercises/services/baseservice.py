class BaseService:
    def setCallback(self, callback):
        if callback is None:
            raise Exception('Invalid Orders Service Callback Specified!')

        self.callback = callback
