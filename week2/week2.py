"""
1.Reverse a string i.e if the string is "boy" the reversed string should be "yob" . 
  There is an inbuilt function in python for this 
  --Given a list of 10 random numbers
2.Find the largest number in the list
3.Remove all duplicate numbers from the list  
4.Sort the list in ascending order
@author Precious Omonzejele 
"""
import random
##function to accept string and print backwords
def acceptThenTurn():
   inp = input("Please type in a string: ")
   inp = str(inp)
   #making it reverse backward , in python use slicing method inp[::-1] to start backwards, they can also use reversed(inp) ish shaa
   print ("printing backwards is : ",inp[::-1])
   return

##random list function
def randTheList():
   iList = []
   for x in range(10):
       randNumber = random.randint(1,100)
       iList.extend([randNumber])
   return iList;#no need to use ; but i just had to, not using curly braces is killing me, if freshi likes, he should come and
   #beat me cause i said braces instead of brackets

#get the largest number in the list, can also use max()
def getHighestNumber(theList):
   high_numb_holder = 0
   #looping
   for x in theList:
      if(x > high_numb_holder): #add to the holder
         high_numb_holder = x
#what it simply does is it loops through the list, and keeps updating the high_numb_holder to the highest number, 
#so if x isnt high, it doesnt bother updating :)
#who needs functions when you can think :)
   return high_numb_holder;
   
###################main start
#####
print("Hello, welcome to this program that does what i say it should do, i'm legit a pythonista :)\n");
acceptThenTurn();
#do some random listing
ourList = randTheList()
print("Our random list of 10 numbers are: ",ourList)
#the largest number in the list
print("The largest number in the list is: ",getHighestNumber(ourList))
#removing duplicates using set(), first check if the list has duplicate, got this from stack overflow, sweet
notDupList = set(ourList);
if(len(notDupList) != len(ourList)):#there was a duplicate
   print("Removing all duplicates, we have ",notDupList)
else:
   print("There's actually no duplicate in our list, so it still remains as: ",ourList)

#sorting list in ascending order
""" how to sort
templist = [25, 50, 100, 150, 200, 250, 300, 33]
sorted(templist, key=int)               # ascending order
> [25, 33, 50, 100, 150, 200, 250, 300]
sorted(templist, key=int, reverse=True) # descending order
> [300, 250, 200, 150, 100, 50, 33, 25]
"""
sortedList = sorted(ourList, key=int)
print("The list in ascending order is as follows : "+str(sortedList))
