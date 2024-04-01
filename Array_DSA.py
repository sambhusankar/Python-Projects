import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ","
        return result[:-1]
        
    def __getitem__(self,index):
        if 0<=index<=self.n:
            return self.A[index]
        else:
            return 'IndexError Out of range'
    def pop(self):
        if self.n>0:
            self.n =self.n-1
        else:
            return 'List is empty nothing to pop'

    def clear(self):
        self.n=0
        self.size=1
        
    def find(self,item):
        for I in range(self.n):
            if self.A[I]==item:
                return I
            else:
                return "Not found"
 

    def insert(self,pos,item):
        if 0>pos or self.n<pos:
            return 'IndexError out of undex'
        if self.n == self.size:
            __resize(self.size*2)
        for I in range(self.n,pos,-1):
            self.A[I]=self.A[I-1]
        self.A[pos]=item
        self.n+=1

    def __delitem__(self,pos):
        for I in range(pos,self.n-1):
            self.A[I]=self.A[I+1]
        self.n-=1
   
    def append(self, item):
        if self.size == self.n:
            # resize
            self.__resize(self.size * 2)
        # append
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __make_array(self, capacity):
        # Returns a C array
        return (capacity * ctypes.py_object)()

L = MyList()
L.append("hi")
L.append("sankar")
L.append("swain")
L.append("DSA")
L.append("Python")
L.append("dhoba")
L.append("anil")
L.insert(2,"sugyani")
print(len(L))
del L[1]
print(L)
index=L.find("sankar")
print(index)
print(L[1])