##Ask the user to enter
##their name and then
##display their name
##three times.

##name=input("Enter your Name:")
##num = int(input("Enter a Number:"))
##for i in range(0,num):
##    print(name)
    
##Ask the user to enter their name and display each letter in
##their name on a separate line.

##name=input("Enter your Name:")
##for i in name :
##    print(i)
##    




##Ask the user to enter their name and display each letter in
##their name on a separate line.
##Change program
##037 to also ask for a
##number. Display
##their name (one
##letter at a time on
##each line) and
##repeat this for the
##number of times
##they entered.



##name = input("Enter your Name:")
##number = int(input("Enter your Number:"))
##for x in range(number):
##    for i in name:
##        print(i)
##
##

##
##Ask Ask the user to enter a number between 1
##and 12 and then display the times table for
##that number

##num = int(input("Enter your Number between 1 and 12:"))
##for i in range(1,21):
##    answer=i*num
##    print(f"{i}*{num}={answer}")




##Ask for a number below 50 and then count down from
##50 to that number, making sure you show the number
##they entered in the output    
##    

##num = int(input("Enter your Number below 50:"))
##for num in range(50,num,-1):
##    print(num)


##Ask the user to enter their
##name and a number. If the
##number is less than 10, then
##display their name that
##number of times; otherwise
##display the message “Too
##high” three times.
##name = input("Enter your name:")
##num = int(input("Enter a number:"))
##if num > 10 :
##    for _ in range(1,4):
##        print("Too high")
##else:
##    for _ in range(1,num+1):
##        print(f"{name}")



##Set a variable called total to 0. Ask the user to enter
##five numbers and after each input ask them if they
##want that number included. If they do, then add the
##number to the total. If they do not want it included,
##don’t add it to the total. After they have entered all five
##numbers, display the total.    


##total = 0
##for i in range(1,6): 
##    num = int(input("Enter your five numbers:"))
##    ask = input("Do you want to include the number(y/n):")
##    if ask == "y":
##        total =total+num
##    elif ask == "n":
##        print(f"{num} is not included")
##    else:
##        print("invalid input")
##        total
##        
##print(f"your total number is :{total}")  



##Ask which
## direction the user wants to count (up or down). If they select up,
##then ask
##them for the top number and th
##en count from 1 to that number. If they select down, ask
##them to enter a number
##below 20 and then count down from 20 to that number. If they
##entered something other than up
##or down, display the message “I don’t understand”.



##ask = input("Do you want to count from (up or down):")
##if ask == "up":
##    topnum = int(input("Enter your top number:"))
##    for i in range(1,topnum+1,+1):
##        print(i)
##elif ask == "down":
##    downnum = int(input("Enter your number below 20 :"))
##    for i in range(downnum,21,+1):
##        print(i)
##else:
##    print("invalid input")



##Ask how many people the user wants to invite to a party. If they enter a number below
##10, ask for the names and after each name display “[name] has been invited”. If they
##enter a number which is 10 or higher, display the message “Too many people”.




invite = int(input("How many people do you want to invite to a party:"))
if invite <= 10:
    for _ in range(1,invite+1):
        name = input("Enter your name:")
        print(f"{name} is invited!!")
else:
    print("Too many peoples")
    
    























