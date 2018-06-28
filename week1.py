"""Write a program that takes in 3 input integers and prints out the average of the numbers
Bonus : try to get the highest of the 3 input numbers and print it out
@author Precious Omonzejele 
"""
print("Hello, welcome to this program that does what i say it should do\n");
inp1 = input("Please select your first number:");
inp2 = input("Please select your second number:");
inp3 = input("please selcet your third number:");
#casting things, too bad , no binding :(
inp1 = int(inp1);
inp2 = int(inp2);
inp3 = int(inp3);

#now process the input, geez i hate python, cant do // to comment :(
while isinstance(inp1,int) == false or isinstance(inp2,int) == false or isinstance(inp3,int()) == false :
	print("please some values arent int, try again\n");
    inp1 = input("Please select your first number:");
	inp2 = input("Please select your second number:");
	inp3 = input("please selcet your third number:");
    #casting things, too bad , no binding :(
	inp1 = int(inp1);
	inp2 = int(inp2);
	inp3 = int(inp3);

#someone cannot use curly braces, have to indent, wth, smh
#now get the average
avg = (inp1 + inp2 + inp3) / 3
print("your first number is "+inp1+"\n Second number is "+inp2+"\n third number is "+inp3+"\n average is : "+avg)
#get the highest number
numb_array = [inp1,inp2,inp3]

