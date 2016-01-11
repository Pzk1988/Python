import time
from datetime import datetime
import timeit

class AmstrongNumber:
    number = 0
    copyOfNumber = 0
    digitList = list()
    result = 0

    def getNumber(self, number):

        self.number = 0
        self.copyOfNumber = 0
        self.digitList = list()
        self.result = 0

        if number != 0:
            self.number = number
            self.copyOfNumber = number
            #print("Checking: ", self.number)
        else:
            print("Number must be diffrent than 0")

    def checkNumber(self):
        temp = 0
        while self.number > 0:
            #print("Reszta ", self.number % 10)
            self.digitList.extend([self.number % 10])
            self.number = int(self.number / 10)
            #print("Zostalo ", self.number)

        #print("W liscie: ", self.digitList, len(self.digitList))
        for i in range(0, len(self.digitList)):
            temp = self.digitList[i]
            #print("temp = ", temp)
            for j in range(0, len(self.digitList) - 1):
                temp *= self.digitList[i]

            #print(temp)
            self.result += temp
            if self.result > self.copyOfNumber:
                #print("Break result: ", self.result, "myNumber: ", self.copyOfNumber)
                break                
        if self.result == self.copyOfNumber:
            print(self.copyOfNumber, " is amstrong number")
        #else:
            #print(self.copyOfNumber, "is not amstrong number")


amstrongNumber = AmstrongNumber()
start_time = time.monotonic()
start_time1 = datetime.now()
start_time2 = timeit.default_timer()

for i in range (1, 100000):
    amstrongNumber.getNumber(i)
    amstrongNumber.checkNumber()
print("--- %s seconds ---" % (time.monotonic() - start_time))
print('Duration: {}'.format(datetime.now() - start_time1))
print("--- %s seconds ---" % (timeit.default_timer() - start_time2))
