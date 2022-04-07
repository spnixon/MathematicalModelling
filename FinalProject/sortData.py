from collections import deque
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class sensReading:
    def __init__(self):
        #-999 used a sentinel value to flag error
        self.temp = -999
        self.FDOY= -999
        self.PAppbv= -999
        self._49Cppbv = -999 #This is the more accurate sensor
        self.readNum = -999

    def print(self):
        print('Number:',self.readNum,'FDOY:',self.FDOY,'Temp:',self.temp,'PA (ppbv):',self.PAppbv,'49C (ppbv):',self._49Cppbv)

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

def scatterPrintRange(sensorData:deque, start:int, end:int):
    x = 0
    while ( x+100 < len(sensorData)-1 ) and ( sensorData[x+100].PAppbv < start ):
        x+=100
    while( x+10 < len(sensorData)-1 ) and ( sensorData[x+10].PAppbv < start ):
       x+=10
    while sensorData[x].PAppbv < start:
       x += 1

    PA = list()
    t49c = list()
    PA.clear()
    t49c.clear()
    while sensorData[x].PAppbv < end: # place x and y axis into seperate lists
        PA.append(sensorData[x].PAppbv)
        t49c.append(sensorData[x]._49Cppbv)
        sensorData[x].print()
        x+=1
    plt.scatter(PA, t49c)
    plt.title('PA vs 49C')
    plt.xlabel('PA ppbv', fontsize=14)
    plt.ylabel('49C ppbv', fontsize=14)
    plt.grid(False)
    plt.show()
    tkPlot = input("Do you want a TKinter Plot?(y/Y): ")
    if tkPlot == 'y' or tkPlot=='Y':
        data = {'PA':PA, '49C':t49c}
        df = DataFrame(data,columns=['PA','49C'])
        root = tk.Tk()
        figure = plt.Figure(figsize=(10,8), dpi=100)
        ax = figure.add_subplot(111)
        ax.scatter(df['PA'],df['49C'],color='g')
        scatter = FigureCanvasTkAgg(figure, root) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax.legend(['49C']) 
        ax.set_xlabel('PA')
        ax.set_title('PA Vs. 49C')
        root.mainloop()
    print('Done')


    
df = pd.read_csv('TempBins_01.csv')
sensorData = deque()
readData = list()
sensorData.clear()
progress = 0
numReadings = 42545
for i in range (0, numReadings):
    if i%4300 == 0:
        progress+=10
        print(progress,'%')
    readData = df.iloc[i]
    newNode = sensReading()
    newNode.FDOY = readData[0]
    newNode._49Cppbv = readData[1]
    newNode.PAppbv = readData[2]
    newNode.temp = readData[3]
    newNode.readNum = i+1
    addItem(sensorData, newNode)
print("Done")

print('Enter the plot range')
start = int(input())
end = int(input())
scatterPrintRange(sensorData, start, end)

