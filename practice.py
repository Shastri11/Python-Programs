

# a=1022003030303
# txt = " Hello World "
# x=txt
# # x=txt.strip()
# print(x) 
# print(type(None))
# print(range(a))
####------------------------------------

#write a program to print pattern in python
# def pyramid(n):               #define a function
#     for i in range(0,n):     # range of i is 0 to 3
#         for j in range(0,i+1):   # increment i by 1 upto n 1.0-1(executed 1 time) 2. 0-2(executed 2 times) 3. 0-3(executed 3 times)
#             print("#",end="")
            
#         print("\r")

# n=3
# pyramid(n)
###------------------------------------
#Use REPL and print the table of 10 using it.
# def table(n):
#     for i in range(0,n):
#         print(10,'x',i,'=',i*10)
        
#     print("\r")

# n=11
# table(n)

#-------------------------------
# type casting
# a=10
# print(type(a))
# b=float(a)
# print(b)
# c='10.7'
# c=float(c)
# print(type(c))
# d=float(c)
# print(type(d))
# e=int(d)
# print(type(e))
# f=None
# print(type(f))
# boolean value true orfalse shall be written as True or False(initial capital); if written in small case or 
# capital it'll not work
# AvalueStr='False'
# print(AvalueStr)
# # print(type(AvalueStr))
# # AvalueStr2=bool(AvalueStr)
# # print(AvalueStr2)
# AvalueStr2 = eval(AvalueStr)
# print(AvalueStr2)

#------------------------------------------
# Operators
# Arithmetic Operators
# x=10
# y=20
# print("answer is",y-x)                  # –	Subtraction: subtracts two operands	x – y 
# print("answer is",x*y) # *	Multiplication: multiplies two operands	x * y
# print("answer is",x/y)# /	Division (float): divides the first operand by the second	x / y
# print("answer is",x//y)# //	Division (floor): divides the first operand by the second	x // y
# print("answer is",x%y)# %	Modulus: returns the remainder when the first operand is divided by the second	x % y
# print("answer is",x**y)# **	Power: Returns first raised to power second	x ** y


# print(int(input("a:"))+int(input("b:")))

aVariable="Welcome"

# print(aVariable[::-1]) #reverse string --emocleW
#or
# aVariable =aVariable[::-1]
# print(aVariable) #reverse string ---emocleW
# # aVariable=isinstance(aVariable,str)
# print("the type of class is:",isinstance(aVariable,str))# false
# print(aVariable)  #True
# print(len(aVariable))
# print(aVariable.endswith("ome"))
# print(aVariable.count("e"))
# print(aVariable.capitalize())
# print(aVariable.find("elc"))
# print(aVariable.replace("Welcome","welcome"))
# print(aVariable)
# print(aVariable.count("Welcome"))

#---------------------------------------
#play sound
# import vlc
# from playsound import playsound
# import time
# p=vlc.MediaPlayer("E:\\Entertainment\\English\\Songs\\top gun songs\\01 - Danger Zone.mp3")
# playsound('E:\\Entertainment\\English\\Songs\\top gun songs\\01 - Danger Zone.mp3') #--not working
# p.play()
# time.sleep(10)
# p.stop()

#---------------------------------------
# Add two numbers
# x=int(input("x:"))
# y=int(input("y:"))
# z=x+y
# print("addition of two numbers:",z)

#----------------------------------------
# Write a Python program to find the remainder when a number is divided by Z(Integer).
# x=int(input("x:"))
# z=int(input("z:"))
# y=x%z
# print("remainder of division:",y)

#-----------------------------------------
#Check the type of the variable assigned using the input() function.
# x=input() #when you take a user input using input() function, it returns string always.
# print(type(x))
# x=10 #<class 'str'>
# x=10.2 #<class 'str'>
# x=abs #<class 'str'>

# y=int(input("enter the value:"))

# if(isinstance(y,float)):
#     print("the variable is of type float.")
# elif(isinstance(y,int)):
#     print("the variable is an integer.")
# elif(isinstance(y,str)):
#     print("the variable is a string.")
# elif(isinstance(y,bool)):
#     print("the variable is boolean")
# else:
#     print("Unknown")

#-----------------------------------------
#Use a comparison operator to find out whether a given variable a is greater than b or not. 
#(Take a=34 and b=80)

# a=34
# b=80
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is smaller than b")
#or
# a=34
# b=80
# if a==b:
#     print("not same")
# elif(a<b):
#     print("smaller")
# else:
#     print("greater")
#------------------------------------------
#Write a Python program to find the average of two numbers entered by the user.
# c=int(input("c:"))
# d=int(input("d"))
# print("average of two numbers is:",(c+d)/2)
#or
# import math
# from statistics import mean

# x=[int(input("a:")),int(input("b:"))]
# y=mean(x)
# print(y)

#----------------------------------------
#Write a Python program to calculate the square of a number entered by the user.
# x=int(input("x"))
# y=int(input("y"))
# print(x,"^",y,'=',x**y)
#-----------------------------------------
#escape characters
#\r Carriage Return
#\n New Line 
#\t tab
#\b backspace
#\' single quote
# email1="Hi \r hru "
# print(email1) #hru
# email1="Hiiiiiiiii \r hru "#hru iiiii comes back to the starting of line and replaces 3 first chracters of the line
# print(email1) #hru
# email1="Hi \n\rhru "
# print(email1)  #Hi (next line) "space" hru
# email1="Hi \r\n\bhru "
# print(email1) #Hi (next line) "space" hru
# email1="Hi \r\n\bhru \bwyd "
# print(email1) #hruwyd -- backspaced 

#-----------------------------------------
#1.Write a program to detect double spaces in a string. (count of double space or count of any char)
# aLine="I have to write  a  line with  double spaces."
# print("doubele space:",aLine.find("  "),aLine.count("  ")) #o/p 15 3

#-----------------------------------------
#Write a program to format the following letter using escape sequence characters.
# email="Dear  Candidate,\n\t We are delight to inform you that you have cleared all rounds of interview \nand we are extending offer to join us.\nThank you,\nHR"
# print(email)
#3.	From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function
# print(email.replace('Candidate','Sushant'),email.replace('HR','Tushar'))

#4.	Replace the double spaces from problem 3 with single spaces.

# email=email.replace("  "," ")
# print(email)

#-------------------------------------------------------
#Lists
#no need to to use assign operator"=" in list while using private property.for ex:thislist.reverse() & not thislist=thislist.reverse()
#thislist.reverse()---right
#thislist=thislist.reverse()  ---wrong syntax
aList=["Hi",10,32,"Hello",True]
# for x in aList:
#     print(type(x))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets  #list constructors
# # print(thislist)

# aList1=list(("Hi,Hello",13,True))
# aList2=["Hi","Hello",13,True]
# print(type(aList1))
# print(aList1[0:2])
# print(aList1)
# aList1.insert(2,"wyd") 
# aList2.insert(2,"wyd")
# print(aList1) #['Hi,Hello', 13, 'wyd', True]
# print(aList2) #['Hi', 'Hello', 'wyd', 13, True]
#when defined in list format in aList 2 insert puts the value in exactly second position i.e after Hello
# but when we use a list constructor it inserts the value after 2nd index position
# aList1.insert(3,"wassup") #insert will insert the data after 3rd position
# print(aList1)
# aList[1]="tanana"
# print(aList)
# # thislist=thislist.append("chungchungdachunga")  #none
# thislist.append("chungchungdachunga") #['apple', 'banana', 'cherry', 'chungchungdachunga']--right syntax
# print(thislist)
# thislist.reverse()
# print(thislist)#['chungchungdachunga', 'cherry', 'banana', 'apple']-- list reversed
# tropical=["pineapple","orange","guava"]
# thislist.extend(tropical)
# print(thislist)
# evergreen=("mangoes",)
# thislist.extend(evergreen)
# print(thislist) #we can extend list with a tuple
# # thislist.remove(2) #position will not work so use pop if u have to mention the position
# thislist.remove("cherry")
# print(thislist)
# thislist.pop(5) # pop uses position to remove items
# print(thislist)
# del thislist[4] #if position is mentioned the specific item is removed by delete command
# print(thislist)
# del thislist
# print(thislist) #it'll show error because you have deleted the list
# thislist.clear()
# print(thislist) #[] --It'll clear thecontents of the list
# print(x) for x in thislist #looping using comprehension will not work
# [print(x) for x in thislist] # loop comprehension ,this syntax will work;shortcut for loop
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True) #['pineapple', 'orange', 'banana', 'apple']
# print(thislist)
# thislist.sort(reverse=False) #['apple', 'banana', 'orange', 'pineapple']
# print(thislist)
# # mylist=list(thislist)
# # # print(mylist)
# # mylist=thislist.copy()
# # print(mylist)
# print(len(thislist))
# print(f"the length of the string is: {len(thislist)}") #new way to print 

#--------------------------------------------
#Tuples
# from unittest import result
# import math
# aTuple = ('apple', 'banana', 'cherry','apple','orange','papaya')
# aTuple1=(12,14,15,17,19,22)
# aTuple=aTuple.count("apple")
# print(aTuple)
# print(f"thecount of all thevalues is:{aTuple}")
# # aTuple.append("orange")
# print(aTuple)
# #As we can see the tuple can't be modified .we have to use casting and convert tuple into list.
# y=list(aTuple1)
# y.append(23)
# aTuple1=tuple(y)
# print(aTuple1)
# print(y)
# # z=list(aTuple)
# # z.append("orange")
# # aTuple=tuple(z)
# # print(aTuple)
# index=aTuple1.index(22)
# print(f"the index of apple is: {index}",) #5 --returns the index of the value
# # Tuple not getting converted when strings are inserted while tuple is getting converted when int values are inserted.
# tuple3=aTuple + aTuple1
# print(tuple3)
 
#----------------------------------
#Dictionaries
# thisDict={"Carname":"ford mustang","speed in km/hr":100,"Engine capacity in cc":1200,"Colour":"blue"}
# print(thisDict)
# print(thisDict["Carname"])
# # print(thisDict["ford mustang"])# keyerror: 'ford mustang'
# print(type(thisDict))
# thisDict={"Carname":"ford mustang GT","speed in km/hr":100,"Engine capacity in cc":1200,"Colour":"blue"}
# print(thisDict)
# thisDict={"Carname":"ford mustang GT","speed in km/hr":100,"Engine capacity in cc":1200,"Colour":"blue","Carname":("ford mustang","hummer")}
# print(thisDict) #{'Carname': ('ford mustang', 'hummer'), 'speed in km/hr': 100, 'Engine capacity in cc': 1200, 'Colour': 'blue'} #does not display duplicate values
# print(type(thisDict["Engine capacity in cc"])) #<class 'int'>
# for x in thisDict():
#     print(x) 
    # displays keys only --Carname
    #speed in km/hr
    #Engine capacity in cc
    #Colour
# x=thisDict.values()
# y=thisDict.keys()
# print(f"keys and values {y}:{x}")  #keys and values dict_keys(['Carname', 'speed in km/hr', 'Engine capacity in cc', 'Colour']):dict_values([('ford mustang', 'hummer'), 100, 1200, 'blue'])
# print(thisDict["Carname"])
# print(thisDict.keys())
# z=thisDict.items() #([('Carname', ('ford mustang', 'hummer')), ('speed in km/hr', 100), ('Engine capacity in cc', 1200), ('Colour', 'blue')])
# print(z)
# thisDict.update({"wheels":"radial"})
# thisDict.update({"torque in N-m":25,"length in mm":1560}) #can add multiple items in a dictionary
# print(thisDict)
# for x,y in thisDict.items():   #print the keys and respective values in order one after the other
#     print(x,y)
    
# # myDict=thisDict.copy() #copies the content of thisDict to myDict
# # print(myDict) 
# myDict=dict(thisDict)  # dict function to copy the contents of thisDict to myDict
# print(myDict)
# print(len(myDict)) #7
# # thisDict.pop("speed in km/hr") #remove particular item
# # print(thisDict)
# # thisDict.popitem() # delets the last item inserted
# # print(thisDict)
# # del thisDict["Engine capacity in cc"]
# # print(thisDict)
# # del thisDict
# # print(thisDict)
# # thisDict.clear()
# # print(thisDict) #{}
# Govindraos_Family={"Sushila":
#     {"Child1":"Prabhakar",
#      "child2":"baby",
#      "child3":"bandu"},
#   "Pramila":
#       {"child1":"baba",
#        "child2":"shashi"}  
# } 
# print(Govindraos_Family)
# for x,y in Govindraos_Family.items():
#     print(x,y)
 
#-----------------------------------------   
# Sets
# thisSet={10,"orange",True,10.4}
# print(thisSet) #{'orange', 10, 10.4, True}--unordered
# # thisSet.update{"red"} #immutable like tuples
# print(thisSet)            
# x=list(thisSet)
# x.append("red")
# thisSet=set(x)  #set converted to list and back to original set 
# print(thisSet)               
# print("orange" in thisSet)
# thisSet.add(1000)# add can add only one item at a time
# # in order to add multiple items use update() 
# print(thisSet)
# y=["red","blue"]
# thisSet.update(y)  #{True, 'blue', 1000, 10, 10.4, 'red', 'orange'}
# print(thisSet)
# poppeditem=thisSet.pop()
# print(f"the popped item is: {poppeditem}")
# thisSet.remove("blue")
# print(thisSet)
# thisSet.discard("red")
# print(thisSet)
# thisSet.clear()
# print(thisSet)
# set1={10,20,42,"integers"}
# set2={10.1,13.2,15.3,20,"float"}
# # set3=set1.union(set2)
# # print(set3)
# # set1.intersection_update(set2)  # will display common records or duplicates
# # print(set1)  #20
# # set1.intersection(set2)
# # print(set1)
# set1.symmetric_difference_update(set2)#{10, 10.1, 42, 13.2, 'integers', 15.3, 'float'} displays unique records
# print(set1)

#--------------------------------------
# # Loops
#while loop
# i=0
# while i<=8:
#     if(i%2==1):
#         print(10,'x',i,'=',10*i)
#     i+=1
# print('end ofwhile loop')   #printing odd number multiplication

# i=1
# while i<20:
#     if (i/i==1 and i/1==i):
#         print(f"the prime number is:{i}")
#     else:
#         print(f"{i} is not a prime number")
#     i=i+1
# print("refer above for list of prime numbers")

#prime numbers between 1 to 20
# minimum = int(input(" Please Enter the Minimum Value: "))
# maximum = int(input(" Please Enter the Maximum Value: "))

# for Number in range (minimum, maximum + 1):
#     count = 0
#     for i in range(2, (Number//2 + 1)): #(Number//2 + 1) means the number greater than half cannot provide
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')

# functions
#arguments & callings in functions
# def my_function(fname):  #fname is an argument
#     print(fname + " Hello World" + " solo world") #hi Hello World solo world
    
# my_function("hi")  #hi Hello World solo world
# my_function("wassup") #wassup Hello World solo world
abc="cre34de90n1ce"

# for i in range(0,len(abc)):
#     if abc[i].isdigit():
#         print(abc[i]) #3 4 9 0 1

# x=0       #sum of numbers in a string
# for i in range(0,len(abc)):
    
#     if abc[i].isdigit()==True:
#         for x in abc[i]:
#             x=x+abc[i]

# print("sum of digits=",x)

# def sum_digits_string(str1):   #sum of numbers in a string
#     sum_digit = 0
#     for x in str1:
#         if x.isdigit() == True:
#             z = int(x)
#             sum_digit = sum_digit + z

#     return sum_digit
     
# print(sum_digits_string("123abcd45"))
# print(sum_digits_string("abcd1234"))       
        
#-------------------------
#recursion  # thefunction calls  itself
import math
# def factorial(n:int):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# n=int(input("enter number"))  # fibonacci series
# sum=0
# n1=0
# n2=1

# if n<=0:
#     print("please enter number greater than zero")
# else:
#     for i in range(0,n):
#         print(sum,end=' ')
#         n1=n2         
#         n2=sum
#         sum=n2+n1

# print(x)
#####------------------------

def func(a,b):
    c=a+b
    print(c)

func(10,12)

x=[2,2,5,65,87,23,42]
square=list(map(lambda a:a*a,x))
print(square)