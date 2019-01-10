class Sender:
    def send(self, receiver, message):
        receiver.receive(self, message)

    def confirm(self, wait):
        self.confirmation_time = wait

    def check(self):
        return self.confirmation_time


class Receiver:
    def __init__(self, wait, id):
        self.wait = wait
        self.id = id

    # The message should consist of a sender id and the message
    def receive(self, sender, message):
        self.message = message
        # self.message = str(self.id) + str(self.message)
        sender.confirm(self.wait)

    def get_message(self):
        return self.message

    def get_id(self):
        assert self.id > 0
        return self.id

    def get_wait(self):
        return self.wait
