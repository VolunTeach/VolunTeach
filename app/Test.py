
from Client import Client
from Tutor import Tutor

import unittest


class Test(unittest.TestCase):

    # def account_constructor_test(self):        
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def account_setters_test(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def account_ timeslot_test(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    
    #functional tests

    #test 1: no tutors have any overlap at all: 
    def test_bestTutor_1(self):
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
        tutor1 = Tutor()
        tutor1.setName("Tutor 1")
        tutor1.setEmail("tutor1@volunteachtutoring.org")
        tutor1.setMaxHours(8)
        tutor1.setTimeSlot(1, 16, 17, 1)
        tutor1.setTimeSlot(2, 14, 16, 1)
        tutor1.setTimeSlot(2, 17, 19, 1)
        tutor1.setTimeSlot(3, 16, 16.5, 1)
        tutor1.setTimeSlot(4, 17.5, 18.5, 1)
        tutor1.setTimeSlot(5, 12.5, 15, 1)

        tutor2 = Tutor()
        tutor2.setName("Tutor 2")
        tutor2.setEmail("tutor2@volunteachtutoring.org")
        tutor2.setMaxHours(6)
        tutor2.setTimeSlot(2, 13.5, 17.5, 1)
        tutor2.setTimeSlot(2, 18, 20, 1)
        tutor2.setTimeSlot(4, 16.5, 18, 1)
        tutor2.setTimeSlot(6, 13.5, 15.5, 1)
        tutor2.setTimeSlot(6, 17, 29, 1)
        
        tutor3 = Tutor()
        tutor3.setName("Tutor 3")
        tutor3.setEmail("tutor3@volunteachtutoring.org")
        tutor3.setMaxHours(4)
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

    # def bestTutor_test2(self):

    # def bestTutor_test3(self):

    # def bestTutor_test4(self):

    # def bestTutor_test5(self):


if __name__ == '__main__':    
    unittest.main()
    test_bestTutor_1()