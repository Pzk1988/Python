number = int(input("Enter maximum value to check "))

data = list()
for i in range(2, number + 1):
    data.extend([i])
#print(data)

for i in range(0, number - 1):
    #print("index ", i, data[i])
    if data[i] != 0:
        j = 2
        temp = data[i] * j
        #print("Start ", temp, j, data[i], i)
        while temp <= number:
            #print(temp, j, data[i])
            data[temp - 2] = 0
            j += 1
            temp = j * data[i]
        #print(number, " ", temp)

for i in range(0, number - 1):
    if data[i] != 0:
        print(data[i], ", ", end="")
            
            
