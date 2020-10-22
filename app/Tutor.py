#VolunTeach Tutoring Services

from app.Account import Account

#this class inherits Account
class Tutor(Account):

    #constructors
    def __init__(self):
        super(Tutor, self).__init__()
        self.clients = ""
        maxHours = 0

    def __init__(self, name, email, avail, subjects, clients, maxHours):
        super(Tutor, self).__init__(name, email, avail)
        self.clients = clients
        self.maxHours = maxHours

    #setters    
    def setClients(self, clients):
        self.clients = clients
        
    def setMaxHours(self, maxHours):
        self.maxHours = maxHours

    #getters
    def getClients(self):
        return self.clients

    def getMaxHours(self):
        return self.maxHours
