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
            x = 0
            while ( x+100 < len(sensorData)-1 ) and ( sensorData[x+100].PAppbv < newNode.PAppbv ):
                x+=100
            while( x+10 < len(sensorData)-1 ) and ( sensorData[x+10].PAppbv < newNode.PAppbv ):
                x+=10
            while sensorData[x].PAppbv < newNode.PAppbv:
                x += 1
            sensorData.insert(x, newNode)

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
progress = 0
for i in range (0, 42545):
    readData = df.iloc[i]
    newNode = sensReading()
    newNode.FDOY = readData[0]
    newNode._49Cppbv = readData[1]
    if i%4300 == 0:
        progress+=10
        print(progress,'%')
    newNode.PAppbv = readData[2]
    newNode.temp = readData[3]
    addItem(sensorData, newNode)
print("Done")
for x in range (0, 42545):
    sensorData[x].print()