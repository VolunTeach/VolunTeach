#VolunTeach Tutoring Services

from abc import ABC, abstractclassmethod
import json
from datetime import datetime, time

#abstract class with subclasses Client and Tutor

class Account(ABC):

    #constructors   

    def __init__(self, name = "", email = "", genAvail = [[0 for j in range(48)] for i in range(7)]):
        self.name = name
        self.email = email
        self.genAvail = genAvail
        self.curAvail = self.genAvail
        # self.subjects = Subjects()
        super().__init__()

    #setters
    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setGenAvail(self, genAvail):
        self.genAvail = genAvail

    def setCurAvail(self, curAvail):
        self.curAvail = curAvail

    #getters
    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getGenAvail(self):
        return self.genAvail

    def getCurAvail(self):
        return self.curAvail    

    #other methods

    #setTimeSlot
    #day - day of the week (0 = Sunday, 6 = Saturday)
    #start - double representing the first 30 minute time slot to be included (0.0 = 12:00 AM, 20.5 = 8:30 PM)
    #end - double representing the first 30 minute time slot to not be included
    def setTimeSlot(self, day, start, end, value):
        start = int(start * 2)
        end = int(end * 2)
        for i in range(start, end):
            self.genAvail[day][i] = value

    #ranges
    #av - an availability 2d array 
    #value - 0 or 1 depending on what value they want to check
    #return a 2d array of ranges with each range subarray having format [int day, int start, int end] with end NOT included
    @staticmethod
    def ranges(av, value):
        #num represents the total number of ranges
        #count keeps track of consecutive time slots
        num = 0
        count = 0
        end = -1
        rang =  [[0 for i in range(3)] for j in range(1)]
        foundRange = [0 for i in range(3)]

        for i in range(7):
            for j in range(48):
                foundRange[0] = i
                count = 0
                if av[i][j] == value:
                    #first found value in serie of consecutive 'value's
                    if count == 0:
                        num += 1
                        foundRange[1] = j
                    #every time av[i][j] = value
                    count += 1                    
                    if j == 47:
                        count = 0
                        end = 48                        
                        foundRange[2] = end
                        rang.append(foundRange)
                    
                #current value of av[i][j] is not equal to value, and the count is at least 1, it is the end of a time range
                elif count > 0:
                    count = 0
                    end = j
                    foundRange[2] = end
                    rang.append(foundRange)

                
        return rang


    #getOverlap
    #returnst he overlapping schedule between two Account objects
    def getOverlap(self, other):
        overlap = [[0 for j in range(48)] for i in range(7)]
        for i in range(7):
            for j in range(48):
                if (self.genAvail[i][j] == 1 and other.genAvail[i][j] == 1):
                    overlap[i][j] = 1
        return overlap

    #getMatchJSON
    #returns the json object with the match and the overlapping schedule between client and match tutor
    #returns a JSON serializable version of the name and schedule information
    def getMatchJSON(self, match):
        ranges = self.ranges(self.getOverlap(match), 1)
        timeRanges = [[0 for i in range(2)] for j in range(len(ranges))]
        for i in range(len(ranges)):
            day = ranges[i][0]
            sHour = (int) (ranges[i][1] / 2.0)
            eHour = (int) (ranges[i][2] / 2.0)
            print ("sHour is ")
            print(sHour)
            print ("eHour is ")
            print(eHour)
            if (ranges[i][1] == 47):
                sMin = 59
            else:
                sMin = ranges[i][1] / 2.0
                sMin -= (int)(sMin)
                sMin = (int)(sMin * 60) 
            if (ranges[i][2] == 47):
                eMin = 59
            else:
                eMin = ranges[i][2] / 2.0
                eMin -= (int)(sMin)
                eMin = (int)(sMin * 60) 
            timeRanges[i][0] = datetime(2019, 3, 4 + day, sHour, sMin, 0, 0, None).__str__()
            timeRanges[i][1] = datetime(2019, 3, 4 + day, eHour, eMin, 0, 0, None).__str__()

        accDict = {'name': 'You matched with ' + match.name, 'schedule' : timeRanges}
        print(accDict)
        return json.dumps(accDict, indent = 4)



    



            