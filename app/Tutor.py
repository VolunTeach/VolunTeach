#VolunTeach Tutoring Services

from app.Account import Account
from app.Subjects import Subjects

#this class inherits Account
class Tutor(Account):

    #constructors
    def __init__(self):
        super().__init__(self)
        self.clients = ""
        maxHours = 0

    def __init__(self, name, email, avail, subjects, clients, maxHours):
        super().__init__(self, name, email, avail)
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
