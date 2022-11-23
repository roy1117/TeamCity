import Pyro4

print('Ready')
uri = input('Please type proper uri')
remote_connection = Pyro4.Proxy(uri)
print(remote_connection.print_name())