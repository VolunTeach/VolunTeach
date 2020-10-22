class Account:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.avail = [[0 for j in range(48)] for i in range(7)]

    def __init__(self, name, email, avail):
        self.name = name
        self.email = email
        self.avail = avail

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setAvail(self, avail):
        self.avail = avail

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getAvail(self):
        return self.avail    