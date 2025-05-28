##Ask for the user’s first name and display the output message
name = input("enter your name:")
print(f"your name is :{name}")





##Ask for the user’s first name and then ask for their surname and display the output message

fname = input("Enter Your First Name:")
sname = input("Enter your surname:")
print(f"your first name is {fname}")
print(f"your surname is {sname}")
print(f"your full name is :{fname}{sname}")
print("arigato for giving your info ..")






##Write code that will display the joke “What do you call a bear with noteeth?” and on the next line display the answer “A gummy bear!” Try to
##create it using only one line of code.

##print("What do you call a bear with noteeth? \n A gummy bear!")


print("hello , i am a tenacious \ni am nothing")






##Ask the user to enter two numbers. Add them together and
##display the answer as

##num = input("enter two numbers :",a,b)
##print(,a+b)
##num1 = int(input("Enter your number:"))
##num2 = int(input("Enter your number:"))
##total = num1 + num2
##print(total)
num1,num2 = map(int,input("enter your number :").split())
print("total :",num1 + num2)







##Ask the user to enter three numbers. Add together the first
##two numbers and then multiply this total by the third

i,j,k = map(int,input("Enter your three numbers (with a space) :").split())
sol = (i+j)/k
print("solution is :",sol)




##Ask how many slices of pizza the user started with and ask how many slices
##they have eaten.Work out how many slices they have left and display
##the answer in a user- friendly format.
ask1 = int(input("how many slices of pizza the user started with :"))
ask2 = int(input("how many slices they have left :"))
eaten = ask1 -ask2
if ask2 == 0:
    print(f"{eaten}-you are not worth for eating a pizza ,fuck it off")
else:
    if eaten > ask1/2 :
        print(f"{eaten}-you almost did it ,just few more pieces ...")
    elif ask2 != 0 and eaten < ask1/2 :
        print(f"{eaten}-gambare !!!,you can do it....")




##Ask the user for their name and their age. Add 1 to their age

name=input("Enter your name:")
age=int(input("Enter your age:"))
age += 1
print(f"{name} next birthday you will be {age}")




##Ask for the total price of the bill, then ask how
##many diners there are. Divide the total bill by the
##number of diners and show how much each
##person must pay.
price = int(input("What's the total price :"))
dinner = int(input("how many dinners we are :"))
ind_price=price/dinner
print(f"your's individual pay for the dinner is : {ind_price}")




##Write a program
##that will ask for a
##number of days
##and then will
##show how many
##hours, minutes
##and seconds are
##in that number of
##days.
days = int(input("Enter the Number of days :"))
hours = days * 24
minutes = days * (24 * 60)
seconds = days * (24 *(60 * 60))
print(f"{days} days contains : {hours} hours. \n{days} days contains : {minutes} minutes.\n{days} days contains : {seconds} seconds . ")




##There are 2,204 pounds in a kilogram. Ask the
##user to enter a weight in kilograms and convert it
##to pounds.
kilo = int(input("Ente the kilogram :"))
##pound = kilo * 2204
print(f"{kilo *2204} pounds")




##Task the user to enter a number over 100 and then enter a number under
##10 and tell them how many times the smaller number goes into the larger
##number in a user-friendly format.
overno = int(input("Enter a Number over 100 :"))
s_no = int(input("Enter a Number under 10 :"))
f_no = overno // s_no
print(f"{s_no} is roamed {f_no} in {overno}")        
