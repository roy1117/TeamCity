import Pyro4
import Pyro4.naming
import threading
import time
import scriptengine

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

    def open_project(self):
        # project = projects.open(r"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\CodeSys\Regis\Project\RegisNPIBuild.project")
        print('Hello world')


daemon = Pyro4.Daemon()     # make a Pyro daemon
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
print('Start name server')
th = threading.Thread(target=Pyro4.naming.startNSloop)
th.start()
print('Name server started')
ns = Pyro4.locateNS()
ns.register("example", uri)
print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
daemon.requestLoop()

