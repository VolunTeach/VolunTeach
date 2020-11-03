from Client import Client
from Tutor import Tutor
from Account import Account

import unittest

class Test(unittest.TestCase):

    """
    Unit Tests:
    The constructors, accessors, and mutators of the Account, Tutor, and Client classes are tested here.
    """

    # Account class unit tests
    def test_account_constructor(self):
        genAvail = [[0 for j in range(48)] for i in range(7)]
        account = Account("Account", "account@volunteachtutoring.org", genAvail)

        self.assertEquals(account.getName(), "Account")
        self.assertEquals(account.getEmail(), "account@volunteachtutoring.org")
        self.assertEquals(account.getGenAvail(), genAvail)
        
    def test_account_setters(self):
        genAvail = [[0 for j in range(48)] for i in range(7)]
        updatedAvail = [[1 for j in range(48)] for i in range(7)]
        account = Account("Account", "account@volunteachtutoring.org", genAvail)

        account.setName("New")
        account.setEmail("new@volunteachtutoring.org")
        account.setGenAvail(updatedAvail)
        account.setCurAvail(updatedAvail)

        self.assertEquals(account.getName(), "New")
        self.assertEquals(account.getEmail(), "new@volunteachtutoring.org")
        self.assertEquals(account.getGenAvail(), updatedAvail)
        self.assertEquals(account.getCurAvail(), updatedAvail)

    def test_account_timeslot(self):
        genAvail = [[0 for j in range(48)] for i in range(7)]
        account = Account("Account", "account@volunteachtutoring.org", genAvail)

        # Represents a time block on Sunday between 12 pm and 2 pm
        account.setTimeSlot(0, 12, 14, 1)

        # creating expected timeblock in another 24 hour, 30 minute interval matrix
        expectedAvail = [[0 for j in range(48)] for i in range(7)]
        expectedAvail[0][24] = 1
        expectedAvail[0][25] = 1
        expectedAvail[0][26] = 1
        expectedAvail[0][27] = 1

        self.assertEquals(account.getGenAvail(), expectedAvail)

    # Tutor class unit tests
    def test_tutor_constructor(self):
        tutorAvail = [[0 for j in range(48)] for i in range(7)]
        tutor = Tutor("Tutor", "tutor@volunteachtutoring.org", tutorAvail, "Algebra", None, 8)

        self.assertEquals(tutor.getName(), "Tutor")
        self.assertEquals(tutor.getEmail(), "tutor@volunteachtutoring.org")
        self.assertIsNone(tutor.getClients())
        self.assertEquals(tutor.getMaxHours(), 8)

    def test_tutor_setters(self):
        tutorAvail = [[0 for j in range(48)] for i in range(7)]
        tutor = Tutor("Tutor", "tutor@volunteachtutoring.org", tutorAvail, "Algebra", None, 8)

        tutor.setClients(["Client 1", "Client 2"])
        tutor.setMaxHours(10)
        tutor.setSubjects("Algebra 2")
        
        self.assertEquals(tutor.getClients(), ["Client 1", "Client 2"])
        self.assertEquals(tutor.getMaxHours(), 10)
        self.assertEquals(tutor.getSubjects(), "Algebra 2")

    # Client class unit tests
    def test_client_constructor(self):
        clientAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", clientAvail, "Algebra", None)

        self.assertIsNone(client.getTutors())

    def test_client_tutor_relation(self):
        testAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", testAvail, "Algebra", {})
        tutor = Tutor("Tutor", "tutor@volunteachtutoring.org", testAvail, "Algebra", None, 8)

        client.addTutor(tutor)
        self.assertEquals(client.getTutors()['tutor@volunteachtutoring.org'], tutor)

        client.removeTutor(tutor)
        self.assertEquals(client.getTutors(), {})

    """
    Functional Tests:
    The tutor-client scheduling algorithm is tested here.
    """

    #test 1: no tutors have any overlap at all - None
    def test_bestTutor_1(self):
        print("\nRunning bestTutor Test 1...")

        #client data
        clientAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", clientAvail, "Algebra", None)
        client.setTimeSlot(0, 14, 16, 1)
        client.setTimeSlot(0, 18, 20, 1)
        client.setTimeSlot(1, 14, 16, 1)
        client.setTimeSlot(1, 17, 19, 1)
        client.setTimeSlot(3, 14, 16, 1)
        client.setTimeSlot(3, 17, 19, 1)
        client.setTimeSlot(4, 14, 16, 1)
        client.setTimeSlot(4, 19, 20, 1)
        client.setTimeSlot(5, 16.5, 22.5, 1)

        #tutor data
        tutor1Avail = [[0 for j in range(48)] for i in range(7)]
        tutor2Avail = [[0 for j in range(48)] for i in range(7)]
        tutor3Avail = [[0 for j in range(48)] for i in range(7)]

        tutor1 = Tutor("Tutor 1", "tutor1@volunteachtutoring.org", tutor1Avail, "Algebra", None, 8)
        tutor1.setTimeSlot(1, 16, 17, 1)
        tutor1.setTimeSlot(2, 14, 16, 1)
        tutor1.setTimeSlot(2, 17, 19, 1)
        tutor1.setTimeSlot(3, 16, 16.5, 1)
        tutor1.setTimeSlot(4, 17.5, 18.5, 1)
        tutor1.setTimeSlot(5, 12.5, 15, 1)

        tutor2 = Tutor("Tutor 2", "tutor2@volunteachtutoring.org", tutor2Avail, "Algebra", None, 6)
        tutor2.setTimeSlot(2, 13.5, 17.5, 1)
        tutor2.setTimeSlot(2, 18, 20, 1)
        tutor2.setTimeSlot(4, 16.5, 18, 1)
        tutor2.setTimeSlot(6, 13.5, 15.5, 1)
        tutor2.setTimeSlot(6, 17, 23, 1)
        
        tutor3 = Tutor("Tutor 3", "tutor3@volunteachtutoring.org", tutor3Avail, "Algebra", None, 4)
        tutor3.setTimeSlot(0, 16, 17.5, 1)
        tutor3.setTimeSlot(1, 16, 17, 1)
        tutor3.setTimeSlot(2, 12, 15, 1)
        tutor3.setTimeSlot(2, 17.5, 19, 1)
        tutor3.setTimeSlot(5, 23, 23.5, 1)
        tutor3.setTimeSlot(6, 8, 13.5, 1)
        tutor3.setTimeSlot(6, 16, 18.5, 1)
        tutor3.setTimeSlot(6, 19, 22.5, 1)

        tutors = {
            tutor1.getEmail() : tutor1,
            tutor2.getEmail() : tutor2,
            tutor3.getEmail() : tutor3
        }

        self.assertIsNone(client.bestTutor(tutors, 1, 2))


    #test 2 - tutor 1 is better than tutor 2 who is better than tutor 3
    def test_bestTutor_2(self):
        print("\nRunning bestTutor Test 2...")
        #client data
        clientAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", clientAvail, "Algebra", None)
        client.setTimeSlot(0, 14, 16, 1)
        client.setTimeSlot(0, 18, 20, 1)
        client.setTimeSlot(1, 14, 16, 1)
        client.setTimeSlot(1, 17, 19, 1)
        client.setTimeSlot(3, 14, 16, 1)
        client.setTimeSlot(3, 17, 19, 1)
        client.setTimeSlot(4, 14, 16, 1)
        client.setTimeSlot(4, 19, 20, 1)
        client.setTimeSlot(5, 16.5, 22.5, 1)

        #tutor data
        tutor1Avail = [[0 for j in range(48)] for i in range(7)]
        tutor2Avail = [[0 for j in range(48)] for i in range(7)]
        tutor3Avail = [[0 for j in range(48)] for i in range(7)]

        tutor1 = Tutor("Tutor 1", "tutor1@volunteachtutoring.org", tutor1Avail, "Algebra", None, 8)
        tutor1.setTimeSlot(1, 14, 16, 1)
        tutor1.setTimeSlot(2, 14, 16, 1)
        tutor1.setTimeSlot(2, 17, 19, 1)
        tutor1.setTimeSlot(3, 14, 16.5, 1)
        tutor1.setTimeSlot(4, 18.5, 20.5, 1)
        tutor1.setTimeSlot(5, 12.5, 15, 1)

        tutor2 = Tutor("Tutor 2", "tutor2@volunteachtutoring.org", tutor2Avail, "Algebra", None, 6)
        tutor2.setTimeSlot(2, 13.5, 17.5, 1)
        tutor2.setTimeSlot(2, 18, 20, 1)
        tutor2.setTimeSlot(4, 14, 20, 1)
        tutor2.setTimeSlot(6, 13.5, 15.5, 1)
        tutor2.setTimeSlot(6, 17, 23, 1)
        
        tutor3 = Tutor("Tutor 3", "tutor3@volunteachtutoring.org", tutor3Avail, "Algebra", None, 4)
        tutor3.setTimeSlot(0, 16, 17.5, 1)
        tutor3.setTimeSlot(1, 16, 17, 1)
        tutor3.setTimeSlot(2, 12, 15, 1)
        tutor3.setTimeSlot(2, 17.5, 19, 1)
        tutor3.setTimeSlot(5, 23, 23.5, 1)
        tutor3.setTimeSlot(6, 8, 13.5, 1)
        tutor3.setTimeSlot(6, 16, 18.5, 1)
        tutor3.setTimeSlot(6, 19, 22.5, 1)

        tutors = {
            tutor1.getEmail() : tutor1,
            tutor2.getEmail() : tutor2,
            tutor3.getEmail() : tutor3
        }
        self.assertEqual(client.bestTutor(tutors, 1, 2).getEmail(), "tutor1@volunteachtutoring.org")

    #test 3 - tutor 1 and 2 are equal, and tutor 3 is worse
    def test_bestTutor_3(self):
        print("\nRunning bestTutor Test 3...")
        #client data
        clientAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", clientAvail, "Algebra", None)
        client.setTimeSlot(0, 14, 16, 1)
        client.setTimeSlot(0, 18, 20, 1)
        client.setTimeSlot(1, 14, 16, 1)
        client.setTimeSlot(1, 17, 19, 1)
        client.setTimeSlot(3, 14, 16, 1)
        client.setTimeSlot(3, 17, 19, 1)
        client.setTimeSlot(4, 14, 16, 1)
        client.setTimeSlot(4, 19, 20, 1)
        client.setTimeSlot(5, 16.5, 22.5, 1)

        #tutor data
        tutor1Avail = [[0 for j in range(48)] for i in range(7)]
        tutor2Avail = [[0 for j in range(48)] for i in range(7)]
        tutor3Avail = [[0 for j in range(48)] for i in range(7)]

        tutor1 = Tutor("Tutor 1", "tutor1@volunteachtutoring.org", tutor1Avail, "Algebra", None, 8)
        tutor1.setTimeSlot(1, 14, 16, 1)
        tutor1.setTimeSlot(2, 14, 16, 1)
        tutor1.setTimeSlot(2, 17, 19, 1)
        tutor1.setTimeSlot(3, 14, 16.5, 1)
        tutor1.setTimeSlot(4, 18.5, 20.5, 1)
        tutor1.setTimeSlot(5, 12.5, 15, 1)

        tutor2 = Tutor("Tutor 2", "tutor2@volunteachtutoring.org", tutor2Avail, "Algebra", None, 6)
        tutor2.setTimeSlot(1, 14, 16, 1)
        tutor2.setTimeSlot(2, 14, 16, 1)
        tutor2.setTimeSlot(2, 17, 19, 1)
        tutor2.setTimeSlot(3, 14, 16.5, 1)
        tutor2.setTimeSlot(4, 18.5, 20.5, 1)
        tutor2.setTimeSlot(5, 12.5, 15, 1)
        
        tutor3 = Tutor("Tutor 3", "tutor3@volunteachtutoring.org", tutor3Avail, "Algebra", None, 4)
        tutor3.setTimeSlot(0, 16, 17.5, 1)
        tutor3.setTimeSlot(1, 16, 17, 1)
        tutor3.setTimeSlot(2, 12, 15, 1)
        tutor3.setTimeSlot(2, 17.5, 19, 1)
        tutor3.setTimeSlot(5, 23, 23.5, 1)
        tutor3.setTimeSlot(6, 8, 13.5, 1)
        tutor3.setTimeSlot(6, 16, 18.5, 1)
        tutor3.setTimeSlot(6, 19, 22.5, 1)

        tutors = {
            tutor1.getEmail() : tutor1,
            tutor2.getEmail() : tutor2,
            tutor3.getEmail() : tutor3
        }
        self.assertEqual(client.bestTutor(tutors, 1, 2).getEmail(), "tutor2@volunteachtutoring.org")

    #test 4 - all tutors are equally good with some overlap
    def test_bestTutor_4(self):
        print("\nRunning bestTutor Test 4...")
        #client data
        clientAvail = [[0 for j in range(48)] for i in range(7)]
        client = Client("Client", "client@volunteachtutoring.org", clientAvail, "Algebra", None)
        client.setTimeSlot(0, 14, 16, 1)
        client.setTimeSlot(0, 18, 20, 1)
        client.setTimeSlot(1, 14, 16, 1)
        client.setTimeSlot(1, 17, 19, 1)
        client.setTimeSlot(3, 14, 16, 1)
        client.setTimeSlot(3, 17, 19, 1)
        client.setTimeSlot(4, 14, 16, 1)
        client.setTimeSlot(4, 19, 20, 1)
        client.setTimeSlot(5, 16.5, 22.5, 1)

        #tutor data
        tutor1Avail = [[0 for j in range(48)] for i in range(7)]
        tutor2Avail = [[0 for j in range(48)] for i in range(7)]
        tutor3Avail = [[0 for j in range(48)] for i in range(7)]

        tutor1 = Tutor("Tutor 1", "tutor1@volunteachtutoring.org", tutor1Avail, "Algebra", None, 8)
        tutor1.setTimeSlot(1, 14, 16, 1)
        tutor1.setTimeSlot(2, 14, 16, 1)
        tutor1.setTimeSlot(2, 17, 19, 1)
        tutor1.setTimeSlot(3, 14, 16.5, 1)
        tutor1.setTimeSlot(4, 18.5, 20.5, 1)
        tutor1.setTimeSlot(5, 12.5, 15, 1)

        tutor2 = Tutor("Tutor 2", "tutor2@volunteachtutoring.org", tutor2Avail, "Algebra", None, 6)
        tutor2.setTimeSlot(1, 14, 16, 1)
        tutor2.setTimeSlot(2, 14, 16, 1)
        tutor2.setTimeSlot(2, 17, 19, 1)
        tutor2.setTimeSlot(3, 14, 16.5, 1)
        tutor2.setTimeSlot(4, 18.5, 20.5, 1)
        tutor2.setTimeSlot(5, 12.5, 15, 1)
        
        tutor3 = Tutor("Tutor 3", "tutor3@volunteachtutoring.org", tutor3Avail, "Algebra", None, 4)
        tutor3.setTimeSlot(1, 14, 16, 1)
        tutor3.setTimeSlot(2, 14, 16, 1)
        tutor3.setTimeSlot(2, 17, 19, 1)
        tutor3.setTimeSlot(3, 14, 16.5, 1)
        tutor3.setTimeSlot(4, 18.5, 20.5, 1)
        tutor3.setTimeSlot(5, 12.5, 15, 1)

        tutors = {
            tutor1.getEmail() : tutor1,
            tutor2.getEmail() : tutor2,
            tutor3.getEmail() : tutor3
        }
        self.assertEqual(client.bestTutor(tutors, 1, 2).getEmail(), "tutor3@volunteachtutoring.org")

if __name__ == '__main__':    
    unittest.main()
