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

    def receive(self, sender, message):
        sender.confirm(self.wait)

    def get_id(self):
        return self.id

    def get_wait(self):
        return self.wait
