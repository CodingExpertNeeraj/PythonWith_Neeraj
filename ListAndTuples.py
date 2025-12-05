# Diffreance between list and tuple
# list
#list [] inse banti hai
myList = [2,5,7,"Neeraj","India",22,"9may",2000]
print(myList)
print(type(myList))
print(myList[6])
myList[4] = "Uttarakhand"
# In list we can change the value..  now we have uttarakhand in place of india.
print(myList)

#tuple
#Tuple () inse banti hai
myTuple = (89,6,754,"tiwari","almora","i am tuple","hope you are getting","samjho bhai")
print(myTuple)
print(type(myTuple))
print(myTuple[5])
# In tuple we can't change again value
# myTuple[3] = "Tiwari".         we will get error!
# print(myTuple)