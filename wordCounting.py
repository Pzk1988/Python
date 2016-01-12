import codecs
import operator
import sys

dictionary = dict()

def openFile(file):
    f = codecs.open(file, 'r', 'utf-8')

    for line in f:
        for word in line.split():
            clearWord = removeNonCharSign(word)
            if len(clearWord) > 0:
                if clearWord in dictionary:
                    dictionary[clearWord] += 1
                    #print(clearWord, "+1 ", dictionary[clearWord])
                else:
                   dictionary[clearWord] = 1
                   #print(clearWord, " new ", dictionary[clearWord])
            
def removeNonCharSign(word):
    tempWord = ""
    for i in word:
        if i.isalpha():
            tempWord += i
    return tempWord
    
#def addToList(word):
    ##print(word)

    
#value = 0
#word = ""
openFile("Pan Tadeusz.txt")
sortedDictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
sortedDictionary.reverse()
for i in range(0, 20):
    sys.stdout.write('"')
    print(sortedDictionary[i][0], end="")
    sys.stdout.write('"')
    print(" wystąpiło ", sortedDictionary[i][1], " razy")

