from threading import Thread
import Pyro4
import time


uri = input("What is the Pyro uri of the greeting object? ").strip()
greeting_maker = Pyro4.Proxy(uri)


class Client(Thread):
    def __init__(self, server):
        super().__init__()
        self.daemon = False
        self.server = server

    def run(self):
        while True:
            command = input("Please give us command")
            if hasattr(self, command) and callable(getattr(self, command)):
                function = getattr(self, command)
                function('Roy')
            else:
                print('There is no such a method existing')

    def get_fortune(self, name):
        self.server.get_fortune(name)


if __name__ == "__main__":
    client = Client(greeting_maker)
    client.start()

