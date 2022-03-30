import pandas as pd

df = pd.read_excel('fileName.xlsx')

class Node:
    def __init__(self):
        #find all the values that need to be placed inside a node
        self.temp = -9999
        self.next = None

class sortedLinkedList:
    def __init__(self):
        self.head = None    
    #May not be able to shove in an entire node
    def addNode(self, newNode):
        current = self.head    
        if current is not None:
            while current.next is not None:
                if current.next.temp > newNode.temp:
                    break
                current = current.next

            newNode.next = current.next
            current.next = newNode
            return 

        elif current is None:
            self.head = newNode
        return


