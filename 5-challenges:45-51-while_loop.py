##again = "yes"
##while again == "yes":
##    print("Hello")
##    again=input("Do your want to loop again?")


##total = 0
##while total<100:
##    num = int(input("enter your number below 100:"))
##    total = total+num
##    print(f"total number is {total}")


##Set the total to 0 to start with. While the total is 50 or less, ask
##the user to input a number. Add that number to the total and
##print the message “The total is… [total]”. Stop the loop when
##the total is over 50.


##total = 0
##while total <=100:
##    num=int(input("Enter your number:"))
##    total += num
##    print(f"The Message is {total}")
    



##Ask the user to enter
##a number. Keep
##asking until they enter
##a value over 5 and
##then display the
##message “The last
##number you entered
##was a [number]” and
##stop the program.




num = 0
while num <5:
    num = int(input("Enter a number:"))
print(f"The last number you entered was a {num}")




##Ask the user to enter a
##number and then enter
##another number. Add these
##two numbers together and
##then ask if they want to add
##another number. If they
##enter “y", ask them to enter
##another number and keep
##adding numbers until they
##do not answer “y”. Once the
##loop has stopped, display
##the total.






##num1 = int(input("Enter a number:"))
##num2 = int(input("Enter an another number:"))
##total = num1 +num2
##while True:
##    ask = input("want to add another number(y/n):")
##    if ask=="y":
##        ask2 = int(input("Enter another number:"))
##        total = total+ask2
##    else:
##        print(f"the total is :{total}")
##        break
        
##print(f"The Total is :{total}")

    
##
##Ask for the name of somebody the user wants to invite
##to a party. After this, display the message “[name] has
##now been invited” and add 1 to the count. Then ask if
##they want to invite somebody else. Keep repeating this
##until they no longer want to invite anyone else to the
##party and then display how many people they have
##coming to the party.      



##count=0
##while True:
##    name = input("Enter the name for inviting:")
##    print(f"{name} has been now invited!!")
##    count = count +1
##    more = input("are you want to invite somebody(y/n):").lower()
##    if more != "y":
##        break
##print(f"{count} are coming to the party.") 






##Create a variable called
##compnum and set the value
##to 50. Ask the user to enter a
##number. While their guess
##is not the same as the
##compnum value, tell them if
##their guess is too low or too
##high and ask them to have
##another guess. If they enter
##the same value as
##compnum, display the
##message “Well done, you
##took [count] attempts”.





##count=0
##compnum=50
##while True:
##    num = int(input("Enter a number:"))
##    count = count +1
##    if num < compnum:
##        print("Your guess is too low...")
##    elif num > compnum:
##        print("Your guess is too high..")
##    else :
##        print(f"well done,you took {count} attempts")
##        break
        

##
##Ask the user to enter a number between
##10 and 20. If they enter a value under 10,
##display the message “Too low” and ask
##them to try again. If they enter a value
##above 20, display the message “Too high”
##and ask them to try again. Keep repeating
##this until they enter a value that is
##between 10 and 20 and then display the
##message “Thank you”.



##num = int(input("Enter a number between 10 and 20:"))
##while num>20 or num<10:
##    if num>20:
##        print("Too High!!")
##    elif num<100:
##        print("Too low!!")
##    num = int(input("try again,Enter a Number:"))
##print("Thank you")
    

##Using the song “10 green bottles”, display the lines “There are [num] green bottles
##hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
##should accidentally fall”. Then ask the question “how many green bottles will be
##hanging on the wall?” If the user answers correctly, display the message “There will be
##[num] green bottles hanging on the wall”. If they answer incorrectly, display the
##message “No, try again” until they get it right. When the number of green bottles gets
##down to 0, display the message “There are no more green bottles hanging on the wall”.
##
##num =10
##while num>0:
##    print(f"There are {num} green bottles hanging on the wall . \n{num} green bottles hanging on the wall.")
##    print("if 1 green bottle should accidentally fall .")
##    num = num-1
##    ask = int(input("how many green bottles will be hanging on the wall:"))
##    if ask == num:
##        print(f"There will be {num} green bottles hanging on the wall")
##    else:
##        while ask != num:
##            ask = int(input("NO, try again.."))
##print("There is no more green bottles hanging on the wall... ")


##import random
##num1 = random.randint(1,100)
##num2 = random.randrange(0,100,5)
##add = num1 + num2
##print(f"{num1}+{num2}={add}")
























