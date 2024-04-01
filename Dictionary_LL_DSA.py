import mmh3
class Node:
    def __init__(self,key,value):
        self.data=value
        self.key=key
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
        
    def __len__(self):
        return self.n
        
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
        
    def traverse(self):
        result=""
        curr=self.head
        while curr != None:
            result=result+str(curr.key) + "->" +str(curr.data) + "   "
            curr =curr.next
        return result[:-1]
        
    def append(self,key,value):
        new_node=Node(key,value)
        if self.head ==None:
            self.head =new_node
            self.n+=1
            return
            
        curr=self.head
        while curr.next != None:
            curr=curr.next
        curr.next=new_node
        self.n+=1
        
      
                
    def clear(self):
        self.n=0
        self.head=None
        
    def del_head(self):
        self.head=self.head.next
        self.n-=1
    def del_tail(self):
        curr=self.head
        if self.head==None:
            return "here is nothing to delete "
        while curr.next.next != None:
           curr= curr.next
        curr.next=None
        self.n-=1
        
    def del_tail(self):
        curr=self.head
        if curr.next==None:
            return self.del_head()
            self.n-=1
        
        while curr.next.next !=None:
            curr=curr.next
        curr.next=None
        self.n-=1
        
    def del_val(self, key):
        curr=self.head
        if curr.key==key:
            self.del_head()
            self.n-=1
            return 
        if curr==None:
            return "Empty Linked List"
        while curr.next !=None:
            if curr.next.key==key:
                break 
            curr=curr.next
        if curr.next ==None:
            return "Not found"
        else:
            curr.next=curr.next.next
            self.n-=1
                
    def search(self,item):
        curr=self.head
        pos=0
        while curr != None:
            
           
            if curr.key ==item:
                return curr
                
            curr=curr.next
            pos+=1
            
        return -1
            
    def __getitem__(self,index):
        curr=self.head
        pos=0
        while curr!=None:
            if pos ==index:
                return curr
            curr=curr.next
            pos+=1
        return 'Index Error'  
        
        
 

class Dictionary:
    def __init__(self,capacity):
        self.size=0
        self.capacity=capacity
        self.buckets=self.make_array(capacity)
        
    def make_array(self, capacity):
        Di=[]
        for I in range(capacity):
            Di.append(LinkedList())
        return Di
        
    def put(self,key,value):
        index=self.hash_value(key)
        data_ll=self.buckets[index]
        data_n=data_ll.search(key)
        if data_n == -1:
             data_ll.append(key,value)
             self.size+=1
        else:
             data_n.data=value
             
        if (self.size/self.capacity)>=2:
             self.rehash()
             
    def rehash(self):
          self.capacity*=2
          old_buckets=self.buckets
          self.size=0
          self.buckets=self.make_array(self.capacity)
          for I in range(len(old_buckets)):
              for j in range(len(old_buckets[I])):
                   node=old_buckets[I][j]
                   key_item=node.key
                   value_item=node.data
                   self.put(key_item,value_item)
                   self.size+=1
                 
             
         
    def hash_value(self,key):
            if isinstance(key,str):
                input_string = key
                hash_value = mmh3.                             hash(input_string)  # Non-cryptographic hash

                # Take the modulo to get a consistent output
                return abs(hash_value) % self.capacity
            if isinstance(key,int):
                return abs(hash(key))%self.capacity
     
    def get(self,key):
         index=self.hash_value(key)
         data_ll=self.buckets[index]
         data_n=data_ll.search(key)
         if data_ll.head==None:
             print('Not Found')
         else:
             if data_n == -1:
                 print('Not Found')
             else:
                 print(data_n.data)
            
    def __len__(self):
          return self.size
            
    def delete(self,key):
            index=self.hash_value(key)
            ll=self.buckets[index]
            ll.del_val(key)
            self.size-=1
            
    def traverse(self):
        result=""
        for I in self.buckets:
            result += I.traverse()
        return result
D=Dictionary(3)
D.put(1,10)
D.put(6,20)
D.put(11,220)
D.put(16,160)
D.put(2,20)
D.put(5,50)
D.put(1,100)
D.put(6,200)
D.put(11,2220)

print(D.traverse())
