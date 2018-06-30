"""Write a program that takes in 3 input integers and prints out the average of the numbers
Bonus : try to get the highest of the 3 input numbers and print it out
@author Precious Omonzejele 
"""
print("Hello, welcome to this program that does what i say it should do\n");

inp1 = input("Please select your first number:")
inp2 = input("Please select your second number:")
inp3 = input("please selcet your third number:")
#first check if they're empty to avoid errors
while inp1 == "" or inp2 == "" or inp3 == "":
   print("please some values are empty, try again\n")
   inp1 = input("Please select your first number:")
   inp2 = input("Please select your second number:")
   inp3 = input("please selcet your third number:")
  
#casting things, too bad , no binding :(
inp1 = int(inp1)
inp2 = int(inp2)
inp3 = int(inp3)

#now process the input, geez i hate python, cant do // to comment :(
while isinstance(inp1,int) == False or isinstance(inp2,int) == False or isinstance(inp3,int) == False :
   print("please some values arent int, try again\n")
   inp1 = input("Please select your first number:")
   inp2 = input("Please select your second number:")
   inp3 = input("please selcet your third number:")
    #casting things, too bad , no binding :(
   inp1 = int(inp1)
   inp2 = int(inp2)
   inp3 = int(inp3)

#someone cannot use curly braces, have to indent, wth, smh
#now get the average
avg = (inp1 + inp2 + inp3) / 3
print("your first number is "+str(inp1)+"\n Second number is "+str(inp2)+"\n third number is "+str(inp3)+"\n average is : "+str(avg))
#get the highest number, I've not finished oh,
""" I'm sure there's a built in function for that max(inp1,inp2,inp3), python people and their laziness, it's useful Shaa ahem rushing
But trash it, amma do it myself ;), I'll write it anyhow jare, not so familiar with creating functions in python
"""
#store the inputs in an array first, smh, this is a list :(
numb_list = [inp1,inp2,inp3]
high_numb_holder = 0
#looping
for x in numb_list:
   if(x > high_numb_holder): #add to the holder
      high_numb_holder = x
#what it simply does is it loops through the list, and keeps updating the high_numb_holder to the highest number, 
#so if x isnt high, it doesnt bother updating :)
#who needs functions when you can think :)
print("\n\n The highest number is: "+str(high_numb_holder))
#hend 	  