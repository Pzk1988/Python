class LinearEquasions:
    iSize = 0
    matrix = {}
    def getSizeOf(self):
        self.iSize = int(input("Enter number of equasions: "))
        
    def createMatrix(self):
        for i in range(self.iSize):
            for j in range(self.iSize + 1):
                print(i, ", ", j, ", ", (i*(self.iSize + 1)) + j) 
                self.matrix[(i*(self.iSize + 1)) + j] = float(input("Enter "))

    def printMatrix(self):
        for i in range(self.iSize):
            print("| ", end="")
            for j in range(self.iSize + 1):
                if j < self.iSize - 1:
                    print(self.matrix[(i*(self.iSize + 1)) + j], " ", end="")
                else:
                    print(self.matrix[(i*(self.iSize + 1)) + j], "| ", end="")
            print("")

    def gauss(self):
        for k in range(self.iSize): #iteracja
            print("k = ", k)
            firstInIteration = self.matrix[(self.iSize + 1) * k]
            for i in range(k, self.iSize): #wiersze
                firstInRow = self.matrix[(self.iSize + 1) * i + k]
                print("i = ", i, ", ", firstInRow)
                for j in range(k, self.iSize + 1): #kolumny
                    if k == i:
                        #print("tu ", self.matrix[(self.iSize + 1) * i + j], "=", self.matrix[(self.iSize + 1) * i + j], "/", firstInRow)
                        self.matrix[(self.iSize + 1) * i + j] = self.matrix[(self.iSize + 1) * i + j] / firstInRow
                        #print(self.matrix[(self.iSize + 1) * i + j], self.matrix[(self.iSize + 1) * i])
                    else:
                        #print("jestem ", self.matrix[(self.iSize + 1) * i + j], "=", self.matrix[(self.iSize + 1) * i + j], "-", firstInRow, "*", self.matrix[(self.iSize + 1) * (i - 1) + j])
                        #print((self.iSize + 1) * i + j, "self.iSize", "+", "1", "*", "i", "+", "j")
                        self.matrix[(self.iSize + 1) * i + j] = self.matrix[(self.iSize + 1) * i + j] - firstInRow * self.matrix[(self.iSize + 1) * k + j]

                self.printMatrix()
                print("")
                    

        
linearEquasion = LinearEquasions()

linearEquasion.getSizeOf()
linearEquasion.createMatrix()
linearEquasion.printMatrix()
print("GAUSS")
linearEquasion.gauss()
