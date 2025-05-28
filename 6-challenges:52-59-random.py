##Display a
##random
##integer
##between
##1 and 100
##inclusive


##import random
##num = random.randint(1,100)
##print(f"{num}")

##Display a
##random
##fruit from
##a list of
##five fruits.


##list1=["Orange","Apple","Grapes","pine"]
##print(random.choice(list1))
####print(list1)



##Randomly choose either heads or tails (“h” or “t”). Ask
##the user to make their choice. If their choice is the same
##as the randomly selected value, display the message
##“You win”, otherwise display “Bad luck”. At the end, tell
##the user if the computer selected heads or tails.



##compPlay=random.choice(["head","tail"])
##usrPlay=input("head or tail,choose one:")
##if compPlay == usrPlay:
##    print("YOU WIN!!")
##else:
##    print("Bad Luck..")
##    print("computer selected:"+compPlay)





##Randomly choose a number between 1 and 5. Ask the user to pick a
##number. If they guess correctly, display the message “Well done”,
##otherwise tell them if they are too high or too low and ask them to pick a
##second number. If they guess correctly on their second guess, display
##“Correct”, otherwise display “You lose”.


##import random
##randChoice=random.randint(1,5)
##usrChoice=int(input("Pick a number between 1 and 5:"))
####if usrChoice == randChoice:
####    print("Well Done!!!")
####else:
##while usrChoice != randChoice:
##    if usrChoice > randChoice:
##        print("Too high")
##    elif usrChoice < randChoice:
##        print("Too low")
##    usrChoice = int(input("Pick another number :"))
##print("Well Done!!!")
##        
##import random
##
##randChoice = random.randint(1, 5)
##usrChoice = int(input("Pick a number between 1 and 5: "))
##
##while usrChoice != randChoice:
##    if usrChoice > randChoice:
##        print("Too high")
##    elif usrChoice < randChoice:
##        print("Too low")
##    usrChoice = int(input("Pick another number: "))
##
##print("Well Done!!!")



##Randomly pick a whole number between 1
##and 10. Ask the user to enter a number and
##keep entering numbers until they enter the
##number that was randomly picked.




##import random
##num1 = random.randint(1,10)
##num2 = int(input("Enter a number between 1 to 10:"))
##while num1 != num2:
##    num2 = int(input("keep try:"))
##print("you picked the same number .Welcome!!!")

##
##Update
##program 056
##so that it
##tells the
##user if they
##are too high
##or too low
##before they
##pick again.



##import random
##num1 = random.randint(1,10)
##num2 = int(input("Enter a number between 1 to 10:"))
##while num1 != num2:
##    if num1 > num2:
##        print("Too Low!!!")
##    else:
##        print("Too High!!!")
##    num2 = int(input("keep try:"))
##print("you picked the same number .Welcome!!!")



##Make a maths quiz that asks five questions by randomly
##generating two whole numbers to make the question
##(e.g. [num1] + [num2]). Ask the user to enter the
##answer. If they get it right add a point to their score. At
##the end of the quiz, tell them how many they got correct
##out of five.




##import random
##
##point = 0
##for _ in range(5):
##    num1 = random.randint(1,100)
##    num2 = random.randint(1,100)
##    print(f"{num1}+{num2}")
##    ans = num1+num2
##    ask = int(input("Enter your Answer:"))
##   
##    if ask == ans:
##        point = point+1
##    else:
##        point = point+0
##print(f"score = {point}")
        
        
##    
##import random
##
##point = 0  # initialize score
##for _ in range(5):  # run the loop 5 times
##    num1 = random.randint(1, 100)
##    num2 = random.randint(1, 100)
##    print(f"{num1} + {num2}")
##    ans = num1 + num2
##    try:
##        ask = int(input("Enter your answer: "))
##        if ask == ans:
##            point += 1  # add 1 point if correct
##    except ValueError:
##        print("Invalid input. Please enter an integer.")
##
##print(f"Score = {point}")    
##    


##Display five colours and ask the user to pick one. If they
##pick the same as the program has chosen, say “Well
##done”, otherwise display a witty answer which involves
##the correct colour, e.g. “I bet you are GREEN with envy”
##or “You are probably feeling BLUE right now”. Ask
##them to guess again; if they have still not got it right,
##keep giving them the same clue and ask the user to
##enter a colour until they guess it correctly.




import random

list1=["blue","red","purple","green","black"]
print(list1)

usrPick = input("Pick one :").strip()
compPick = random.choice(list1)

while usrPick.lower() != compPick.lower():
    match compPick:
        case "blue":
            print("I Think You could use blue...")
        case "red":
            print("Holy Shit , Why don't you Pick ReD!!")
        case "purple":
            print("Did you foget about the wonderful Purple...")
        case "green":
            print("I Think you love Nature fav Green!!")
        case "black":
            print("didn't you Batman fan ...")
    usrPick = input("Guess it again!!:")
print("Well Done!!!")



##
##import random
##
##list1 = ["Blue", "Red", "Purple", "Green", "Black"]
##print(list1)
##
##compPick = random.choice(list1)  # Keep case for output
##usrPick = input("Pick one: ").strip()
##
##while usrPick.lower() != compPick.lower():
##    match compPick:
##        case "Blue":
##            print("I think you could use blue...")
##        case "Red":
##            print("Holy Shit, why don't you pick ReD!!")
##        case "Purple":
##            print("Did you forget about the wonderful Purple...")
##        case "Green":
##            print("I think you love nature's fav: Green!!")
##        case "Black":
##            print("Aren't you a Batman fan... Black is the way!")
##    usrPick = input("Guess it again!!: ").strip()
##
##print("Well Done!!!")























