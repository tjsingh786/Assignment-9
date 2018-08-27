#Que1
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as message:
    print(message)

#Que2
#The exception in this program is IndexError
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)

#Que3
  An exception
  NameError:Hi there

#Que4
 -5.0
    a/b result in 0

#Que5
#1. Import Error
try:
  from abc import a
  print(a)
except ImportError:
  print("Error occured:")

#2. Value Error
try:
  num=int(input("Enter number: "))
  print(num)
except ValueError:
  print("Value Error")

#3. Index Error
l=[5,1,2,4]
try:
  print(l[5])
except IndexError:
  print(" Index Error")
