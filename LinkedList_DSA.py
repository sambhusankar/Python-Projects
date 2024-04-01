class Node:
    def __init__(self,value):
        self.data=value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
        
    def __len__(self):
        return self.n
        
        
L=LinkedList()
print(len(L))