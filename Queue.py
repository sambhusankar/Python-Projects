class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def enqueue(self,value):
        new_node=Node(value)
        if self.rear==None:
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node
            
    def dequeue(self):
            if self.rear==None:
                print("Empty Queue")
            else:
                self.front=self.front.next
                
    def size(self):
            curr=self.front
            size=0
            while curr !=None:
                size+=1
                curr=curr.next
            print(size)
            
    def traverse(self):
        curr=self.front
        res=""
        while curr !=None:
            res=res+str(curr.data) +"-"
            curr=curr.next
        print(res[:-1])
