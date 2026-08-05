# movie=[]
# mov1=str(input("Enter the first move: "))
# mov2=str(input("Enter the second move: "))
# mov3=str(input("Enter the third move: "))

# # list=[mov1,mov2,mov3]
# movie.append(mov1)
# movie.append(mov2)      
# movie.append(mov3)
# print(movie)

# tuple=("c","d","a","a","b","b","a")
# print(tuple.count("a"))
# print(tuple.count("b")) 
# print(tuple.count("c"))
# print(tuple.count("d"))

# list=["c","d","a","a","b","b","a"]
# print(list.sort())
# print(list)

# dic={

# }
# sub1=int(input("Enter the marks of subject 1: "))
# sub2=int(input("Enter the marks of subject 2: "))   
# sub3=int(input("Enter the marks of subject 3: "))
# dic["subject1"]=sub1
# dic["subject2"]=sub2        
# dic["subject3"]=sub3
# print(dic)

# i=1
# while i<=10:
#     print(3*i)
#     i+=1

# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(num):
#     print(num[i])
#     i+=1

# num=[1,4,9,16,25,36,49,64,81,100]
# i = 0
# x = 36
# while i < len(num):
#     if num[i] == x:
#         print("Found")
#     else:
#         print("Not Found")
#     i += 1

 
# tup=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# x=36
# for val in tup:
#    if(val == x):
#        print("Found at index:",idx)
#    idx+=1

# sum=int(input("Enter the number: "))
# i=0
# total=0
# while i<=sum:
#     total+=i
#     i+=1
# print(total)    

# n=5
# tot=0
# for i in range(1,n+1):
#     tot+=i
# print(tot)

# n=int(input("Enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)                   

# cities=["Delhi","Mumbai","Chennai","Kolkata","Bangalore"]
# car=["Audi","BMW","Mercedes","Lexus","Porsche"]
# def count(cities):
#    print(cities,car,end=" ")
# count(cities)
# count(car)

# num=int(input("Enter the number: "))

# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#        fact*=i
#        i+=1
#     return fact
# print(fac(num))

# f= open("practice.text","r")
# data=f.read()
# print(data)

# f= open("practice.text","w")
# f.write("python is more suitable then java")
# f.close()

# f= open("practice.text","r+")
# f.write("python is best")
# print(f.read())
# f.close()

# with function

# def replace_word():
#     with open("practice.text","r") as file:
#         data=file.read()
#         newdata=data.replace("java","python")
#         print(newdata)

# replace_word()

# with open("practice.text","r") as file:
#     data=file.read()
#     if(data.find("learning") != -1):
#         print("Found")
#     else:        print("Not Found")


# def search_word():
#     word="learning"
#     data=True
#     count=1
#     with open("practice.text","r") as f:
#         while data:
#             data=f.readline()
#             if(data.find(word) != -1):
#                print("Found on line",count)
#             count+=1
#     return-1    

# search_word()



# count=0
# with open("practice.text","r") as f:
#     x=f.read()
#     y=x.split(",") 
#     for i in y:
#      if (int(i) % 2 == 0):
#         count+=1
      
# print(count)

# class & object

# class student:
#     name="pawan"
#     # it is a constructor
#     def __init__(self,fullname,marks):  
#         self.name=fullname
#         self.marks=marks
#         print("adding a new element")
    
    

# s1=student("kunal",83)
# print(s1.name,s1.marks)

# s2=student()
# print(s2.name)



# class student:
#     def __init__(self,fullname,marks):  
#         self.name=fullname
#         self.marks=marks
        
#     def welcome(self):
#         print("welcome student",self.name)
#     def get_marks(self):
#         return self.marks   
    

# s1=student("kunal", 83)
# s1.welcome()
# print(s1.get_marks())

# class student:
#         # if we use staticmethod then don't use self
#     @staticmethod       
#     def __init__(fullname,marks):  
#         fullname="pawan thakre"
#         marks=[99,98,97]
#         sum=0
#         for val in marks:
#             sum+=val
#         print("hi",fullname,"your average is",sum/3)
    
     
# s1=student("pawan thakre",[99,98,97])


# class student:
#     def __init__(self,name):
#       self.name=name


# s1=student("pawan")
# print(s1.name)
# del s1.name
# print(s1.name)

# class student:
#     def __init__(self,name):
#       self.name=name
#     #   private attribute & method __
#     def __hello(self):
#        print("hello welcome")
#     def welcome(self):
#        self.__hello()

# s1=student("pawan")
# print(s1.welcome())

# inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car start")
#     @staticmethod
#     def stop():
#         print("car stop")
# class toyota(car):
#     def __init__(self,brand):
#         self.brand=brand
# class fortuner(toyota):
#     def __init__(self,type):
#         self.type=type

    

# single level inheritance
# car1=toyota("fortuner")
# car2=toyota("maruti")
# print(car1.start())

# multilevel
# car1=fortuner("desile")
# print(car1.start())

# multiple level
# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class C"

# c1=C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


# super() constructor

# class car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car start")
#     @staticmethod
#     def stop():
#         print("car stop")
# class toyota(car):
#     def __init__(self,brand,type):
#         super().__init__(type)
#         self.brand=brand

# car1=toyota("fortuner","electric")
# print(car1.type)


# class person:
#     name="anonymous"
    
    # def changename(self,name):
        # self.name=name
        # person.name=name
        # self.__class__.name=name
#     @classmethod
#     def changename(cls,name):
#         cls.name=name


# p1=person()
# p1.changename("pawan")
# print(p1.name)
# print(person.name)

# class student:
#     def __init__(self,phy,mth,che):
#         self.phy=phy
#         self.che=che
#         self.mth=mth
#     @property
#     def percentage(self):
#         return str((self.phy+self.che+self.mth)/3)+"%"
        
# s1=student(98,97,99)
# print(s1.percentage)

# s1.phy=86
# print(s1.percentage)



# import random
# ran=random.randint(1,100)

# while True:
#     userchoice=int(input("guess the number:"))
#     if(userchoice == ran):
#         print("you guess the correct number")
#     if(userchoice<ran):
#         print("your number is small guess bigger number")
#     else:print("your number is higer guess smaller number")

# print("----Game is end-----")

         