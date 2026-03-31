import ctypes

class Array:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__ (self):
        return self.n    
    
    def __str__(self):
        result =' '
        for i in range(self.n):
            result += str(self.A[i])  + ','
        return '[' + result[:-1] + ']'
    

    def __getitem__(self, index):
        if 0 <= index < self.n:
           return self.A[index]
        else:
            return 'Indexerror: Index out of range'
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
    
    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()
    
    
 

l=Array()
l.append("Hello")
l.append(3.14)
l.append(True)   
l.append(4)
print(str(l))
print(l[0])
print(l[1])