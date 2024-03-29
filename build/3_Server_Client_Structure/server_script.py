import Pyro4
import threading
import scriptengine

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        print("Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name))

daemon = Pyro4.Daemon()     # make a Pyro daemon
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
th = threading.Thread(target=daemon.requestLoop)
th.start()
