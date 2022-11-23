import Pyro4
import time
@Pyro4.expose
class Student(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print('start')
        time.sleep(30)
        print('wake up')
        return self.name

daemon = Pyro4.Daemon()
uri = daemon.register(Student('Taehyun'))

print('Ready, URI = {0}'.format(uri))
daemon.requestLoop()