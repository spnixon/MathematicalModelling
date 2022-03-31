import pandas as pd
df = pd.read_excel('fileName.xlsx')

class sensReading:
    def __init__(self):
        #-9999 used a sentinel value to flag error
        self.temp = -9999
        self.FDOY = -9999
        self.PAppbv = -9999
        self._49Cppbv = -9999
        self.next = None
    
    def printNode(self):
        print(self.FDOY + ' ' + self.temp + ' ' + self.PAppbv + ' ' + self._49Cppbv)


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


