from re import I
import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name, jurusan):
        # return ("Euy  " + str (name))
        # if age >= 18:
        #     return("Euy " + str (name)+ ' anjeun teh kolot')
        # else :
        #     return("Euy " + str (name)+ ' anjeun teh budak ngora')
        if jurusan in ['d4ti', 'D4TI', 'd4-ti', 'D4-TI']:
            return('euy '+ str(name)+ ' ajeun budak IT gening')
        if jurusan in ['d4lb', 'D4LB', 'd4-lb', 'D4-LB']:
            return('euy '+ str(name)+ ' ajeun budak LB gening')
        if jurusan in ['d4ak', 'D4AK', 'd4-ak', 'D4-Ak']:
            return('euy '+ str(name)+ ' ajeun budak Ak gening')
        else:
            return('ai anjeun teh '+ str(name)+ ', kuliah di mana')

def startServer():
    server = Server()
  
    daemon = Pyro4.Daemon()    # make a Pyro daemon           
   
    ns = Pyro4.locateNS() # locate the name server running
   
    uri = daemon.register(server)   # register the server as a Pyro object
   
    ns.register("server", uri)  # register the object with a name in the name server  
    
    print("Ready. Object uri =", uri)# print the uri so we can use it in the client later
    
    daemon.requestLoop()  # start the event loop of the server to wait for calls                 

if __name__ == "__main__":
    startServer()

