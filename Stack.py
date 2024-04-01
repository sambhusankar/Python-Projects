class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
      
    def isEmpty(self):
        return self.top==None
                      
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        
    def traverse(self):
        curr=self.top
        while curr !=None:
            print(curr.data)
            curr=curr.next
            
    def peek(self):
        if(self.isEmpty()):
            print('Empty Stack')
        else:
            print(self.top.data)
            
    def pop(self):
        if(self.isEmpty()):
            print('Empty Stack')
        else:
            self.top=self.top.next
            
    def reverse(self):
        curr=self.top
        prev=None
        while curr != None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            
        self.top=prev
        
    def str_rev(self,str):
        
        for I in str:
            self.push(I)
        result=""
        while ( not self.isEmpty()):
            result=result+ self.top.data
            self.pop()
        print(result)
            
            
S=Stack()     
S.traverse()
def text_editor(text,pattern):
    u=Stack()
    r=Stack()
    for I in text:
        u.push(I)
    for I in pattern:
        if I =="u":
            r.push(u.top.data)
            u.pop()
        else:
            u.push(r.top.data)
            r.pop()
    curr=u.top
    res=""
    while curr !=None:
        res=curr.data+res
        curr=curr.next
    print(res)

