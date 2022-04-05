import pandas as pd

class sensReading:
    def __init__(self):
        #-9999 used a sentinel value to flag error
        self.temp = -999
        self.FDOY= -999
        self.PAppbv= -999
        self._49Cppbv = -999 #This is the more accurate sensor

def addItem(sensorData:list, newNode:sensReading):
    endIndex = len(sensorData)

    if endIndex == 0 or sensorData[endIndex-1].PAppbv < newNode.PAppbv:
        sensorData.append(newNode)
    else:
        i = 0
        while sensorData[i].PAppbv < newNode.PAppbv:
            i += 1
        sensorData.insert(i, newNode)

def sortBins(sensorData:list, start:int, end:int):
    for i in sensorData:
        if i.temp <= end and i.temp >= start:
            i.printNode(i)
        elif i.temp>end:
            break
    
df = pd.read_csv('TempBins_01.csv')
sensorData = list()
readData = list()
sensorData.clear()
for i in range (0, 5):
    #print(i)
    readData = df.iloc[i]
    #print(readData)
    #print('working 1')
    newNode = sensReading()
    newNode.FDOY = readData[0]
    newNode._49Cppbv = readData[1]
    #print('working 2')
    newNode.PAppbv = readData[2]
    newNode.temp = readData[3]
    #print('working 3')
    addItem(sensorData, newNode)
    #print('working 4')
print("Done")


             

#print(df.head())


#class sortedLinkedList:
#    def __init__(self):
#        self.head = None    
    #May not be able to shove in an entire node into a list so keep this
#    def addNode(self, newNode):
#        current = self.head    
#        if current is not None:
#            if current.temp > newNode.temp:
#               newNode.next = current
#                self.head = newNode
#            else:
#                while current.next is not None:
#                    if current.next.temp > newNode.temp:
#                        break
#                   current = current.next

#                newNode.next = current.next
#                current.next = newNode
#            return 

#        elif current is None:
#            self.head = newNode
#        return


