import mmh3
class Dictionary:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size
        
    def put(self,key,value):
        index=self.hash_value(key)
        if self.slots[index]==None:
            self.slots[index]=key
            self.data[index]=value
        else:
            if self.slots[index]==key:
                self.data[index]=value
            else:
                n_index=(index+1)%self.size
                while self.slots[n_index]!=None and self.slots[n_index]!=key:
                    n_index=(n_index+1)%self.size
                    #self.slots[n_index]=key
                    #self.data[n_index]=value
                if self.slots[n_index]==None:
                    self.slots[n_index]=key
                    self.data[n_index]=value
                else :
                    self.data[n_index]=value
               
    def __setitem__(self,key,value):
        self.put(key,value)          
        
    def get(self,key):
        index=self.hash_value(key)
        start_pos=index
        while self.slots[start_pos] !=None:
            if self.slots[start_pos]==key:
                return self.data[start_pos]
            start_pos=(start_pos+1)%self.size
            if index==start_pos:
                return 'Not Found'
        return 'Not Found'
        
    def __getitem__(self,key):
        return self.get(key)
        
    def __str__(self):
        for I in range(len(self.slots)):
            if self.slots[I] !=None:
                print(self.slots[I]," : ", self.data[I],end=",\n")
        return ''
                
        
                
                
    def hash_value(self,key):
        input_string = key
        if type(input_string)==str:
            hash_value = mmh3.                             hash(input_string)  # Non-cryptographic hash

            # Take the modulo to get a consistent output
            output = abs(hash_value) % self.size
            return output
        
        if type(input_string)==int:
            return abs(hash(input_string))%self.size
        
D=Dictionary(4)
D["ram"]="sita"
D["radha"]="krishna"
D["laxmi"]="narayan"
D["moti"]="motu"
print(D.slots)
print(D.data)
print(D["ram"])
print(D)


