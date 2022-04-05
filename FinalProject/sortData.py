from collections import deque
import pandas as pd

class sensReading:
    def __init__(self):
        #-999 used a sentinel value to flag error
        self.temp = -999
        self.FDOY= -999
        self.PAppbv= -999
        self._49Cppbv = -999 #This is the more accurate sensor

    def print(self):
        print('FDOY:',self.FDOY,'Temp:',self.temp,'PA (ppbv):',self.PAppbv,'49C (ppbv):',self._49Cppbv)

def addItem(sensorData:deque, newNode:sensReading):
    if len(sensorData) != 0:
        if sensorData[-1].PAppbv < newNode.PAppbv:
            sensorData.append(newNode)
        elif newNode.PAppbv < sensorData[0].PAppbv:
            sensorData.appendleft(newNode)
        else:
            i = 0
            while sensorData[i].PAppbv < newNode.PAppbv:
                i += 1
            sensorData.insert(i, newNode)
    elif len(sensorData) == 0:
        sensorData.append(newNode)
    

def sortBins(sensorData:deque, start:int, end:int):
    for i in sensorData:
        if i.temp <= end and i.temp >= start:
            i.printNode(i)
        elif i.temp>end:
            break
    
df = pd.read_csv('TempBins_01.csv')
sensorData = deque()
readData = list()
sensorData.clear()
for i in range (0, 1500):
    print(i)
    readData = df.iloc[i]
    newNode = sensReading()
    newNode.FDOY = readData[0]
    newNode._49Cppbv = readData[1]
    newNode.PAppbv = readData[2]
    newNode.temp = readData[3]
    addItem(sensorData, newNode)
print("Done")
for x in range (0, 1500):
    sensorData[x].print()