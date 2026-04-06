# import ctypes
# from operator import index

# <--Array-->

# class Array:
#     def __init__(self):
#         self.size = 1
#         self.n = 0
#         self.A = self.__make_array(self.size)

#     def __len__ (self):
#         return self.n    
    
#     def __str__(self):
#         result =''
#         for i in range(self.n):
#             result += str(self.A[i]) + ','
#         return '[' + result[:-1] + ']'
    

#     def __getitem__(self, index):
#         if 0 <= index < self.n:
#            return self.A[index]
#         else:
#             return 'Indexerror: Index out of range'
        
#     def append(self, item):
#         if self.n == self.size:
#             self.__resize(self.size*2)
#         self.A[self.n] = item
#         self.n += 1
    
#     def pop(self):
#         if self.n == 0:
#             return 'Indexerror: Array is empty'
#         else:
#             item = self.A[self.n-1]
#             self.n -= 1
#             return item
            
#     def clear(self):
#         self.size = 1
#         self.n = 0

#     def find(self, item):
#         for i in range(self.n):
#             if self.A[i] == item:
#                 return i
#         return "Item not found in array"  

#     def insert(self, index, item):
#         if index < 0 or index > self.n:
#             return 'Indexerror: Index out of range'
#         if self.n == self.size:
#             self.__resize(self.size*2)
#         for i in range(self.n, index, -1):
#             self.A[i] = self.A[i-1]
#         self.A[index] = item
#         self.n += 1

#     def __delitem__(self, index):
#         for i in range(index, self.n-1):
#             self.A[i] = self.A[i+1]
#         self.n -= 1
      
#     def remove(self, item):
#         self.__delitem__(self.find(item))
       
#     def sort(self):
#       for i in range(self.n):
#           if self.A[i]>self.A[i+1]:
#             return self.A[i]
#           else:
#             return self.A[i+1]
          
#     def max(self):
#         max=self.A[0]
#         for num in self.A:
#             if num > max:
#                 max = num
#         return max
                
#     def min(self):
#         min=self.A[0]
#         for num in self.A:
#             if num < min:
#                 min = num
#         return min
    

#     def sum(self):
#         total = 0
#         for num in self.A:
#             total += num
#         return total
    
#     def extend(self, *items):
#      for item in items:
#         self.append(item)


#     def __resize(self, new_capacity):
#         B = self.__make_array(new_capacity)
#         self.size = new_capacity
#         for i in range(self.n):
#             B[i] = self.A[i]
#         self.A = B
    
#     def __make_array(self, capacity):
#         return (capacity*ctypes.py_object)()
    
    
 

# l=Array()
# l.append(1)
# l.append(2)
# l.append(3)   
# l.append(4)
# print(str(l))
# print(l[0])
# print(l[1])
# l.pop()
# l.clear()
# len(l)
# print(l.find(4))
# l.insert(1,23)
# del l[1]
# l.remove(3.14))
# l.sort()
# print(l.max())
# print(l.min())
# print(l.sum())
# l.extend(22,33,55)
# print(l)


# <--LinnkedList-->

class node:

    def __init__(self,value):
        self.value=value
        self.next=None


class Linkendlist:

    def __init__(self):
        self.head=None
        self.n=0

    def __len__ (self):
        return self.n 
    
    def insert_head(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1

    def __str__(self):
        curr=self.head
        result=' '
        while curr!=None:
            result+=str(curr.value) + '-->'
            curr=curr.next
        return result[:-3]










l=Linkendlist()
l.insert_head(22)
l.insert_head(23)
l.insert_head(24)

print(l)    

