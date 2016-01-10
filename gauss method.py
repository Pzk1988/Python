class LinearEquasions:
    iSize = 0
    matrix = {}
    def getSizeOf(self):
        self.iSize = int(input("Enter number of equasions: "))
        
    def createMatrix(self):
        for i in range(self.iSize):
            for j in range(self.iSize + 1):
                print(i, ", ", j, ", ", (i*(self.iSize + 1)) + j) 
                self.matrix[(i*(self.iSize + 1)) + j] = int(input("Enter "))

    def printMatrix(self):
        print(self.iSize)
        for i in range(self.iSize):
            print("|", end="")
            for j in range(self.iSize + 1):
                if j < self.iSize - 1:
                    print(self.matrix[(i*(self.iSize + 1)) + j], " ", end="")
                else:
                    print(self.matrix[(i*(self.iSize + 1)) + j], "|", end="")
            print("")

linearEquasion = LinearEquasions()

linearEquasion.getSizeOf()
linearEquasion.createMatrix()
linearEquasion.printMatrix()
