import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("Ngaran anjeun teh saha? ")
# age = int(input('Sabaraha umur anjeun? '))
jurusan = str(input('jurusan anjeun teh naon? '))
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name,jurusan))




