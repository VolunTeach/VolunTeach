#VolunTeach Tutoring Services

from Account import Account


#this class inherits Account
class Tutor(Account):

    #constructors
    

    def __init__(self, name, email, avail, subjects = "", clients = {}, maxHours = 0):
        super(Tutor, self).__init__(name, email, avail)
        self.clients = clients
        self.maxHours = maxHours

    #setters    
    def setClients(self, clients):
        self.clients = clients
        
    def setMaxHours(self, maxHours):
        self.maxHours = maxHours

    def setSubjects(self, subjects):
        self.subjects = subjects

    def setEmail(self, email):
        self.email = email

    #getters
    def getClients(self):
        return self.clients

    def getMaxHours(self):
        return self.maxHours

    def getSubjects(self):
        return self.subjects

    def getEmail(self):
        return self.email
    


    #hard code values for starter tutors
    #self is not a parameter because these are static functions
    @staticmethod
    def getTutor1():
        avail1 = [[0 for j in range(48)] for i in range(7)]
        for i in range(len(avail1)):
            for j in range(26, 30):
                avail1[i][j] = 1
            for k in range(32, 36):
                avail1[i][k] = 1
            for l in range(38, 42):
                avail1[i][l] = 1
            for m in range(44, 48):
                avail1[i][m] = 1
        return Tutor("Tutor 1", "tutor1@volunteachtutoring.org", avail1, "Algebra", None, 8)
    
    @staticmethod
    def getTutor2():
        avail2 = [[0 for j in range(48)] for i in range(7)]
        for i in range(len(avail2)):
            for j in range(26, 28):
                avail2[i][j] = 1
            for k in range(34, 36):
                avail2[i][k] = 1
            for l in range(42, 44):
                avail2[i][l] = 1
        return Tutor("Tutor 2", "tutor2@volunteachtutoring.org", avail2, "Algebra", None, 6)

    @staticmethod
    def getTutor3():
        avail3 = [[0 for j in range(48)] for i in range(7)]
        for i in range(len(avail3)):
            for j in range(26, 34):
                avail3[i][j] = 1
        return Tutor("Tutor 3", "tutor3@volunteachtutoring.org", avail3, "Algebra", None, 4)



            