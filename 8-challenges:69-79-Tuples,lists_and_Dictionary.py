##Create a tuple containing the names of five countries and display the whole tuple. Ask
##the user to enter one of the countries that have been shown to them and then display
##the index number (i.e. position in the list) of that item in the tuple.

##country=("India","Norway","finland","sweden","iceland")
##print(country)
##print()
##usrreply=input("Enter one of the favourite country above:")
##print(country.index(usrreply))



##Add to program 069 to ask the
##user to enter a number and
##display the country in that
##position.

##country=("India","Norway","finland","sweden","iceland")
##usrNo=int(input("Enter a number below 5:"))
##print(country[usrNo])


##Create a list of two sports. Ask the
##user what their favourite sport is and
##add this to the end of the list. Sort the
##list and display it.


##
##sport=["cricket","football",]
##print(sport)
##usrFav=input("Enter your favourite sport:")
##sport.append(usrFav)
##print(sorted(sport))

##Create a list of six school subjects. Ask the user which of these
##subjects they don’t like. Delete the subject they have chosen from the
##list before you display the list again.


##subject=["Tamil","English","Maths","Science","SocialScience"]
##favSub=input("which subject you not liked ? ")
##subject.remove(favSub)
##print(subject)


##Ask the user to
##enter four of their
##favourite foods
##and store them in
##a dictionary so
##that they are
##indexed with
##numbers starting
##from 1. Display
##the dictionary in
##full, showing the
##index number
##and the item. Ask
##them which they
##want to get rid of
##and remove it
##from the list. Sort
##the remaining
##data and display
##the dictionary.


##fooddic={}
##
##food1=input("Enter your favourite dish:")
##fooddic[1]=food1
##food2=input("Enter another favourite dish:")
##fooddic[2]=food2
##food3=input("Enter another favourite dish:")
##fooddic[3]=food3
##food4=input("Enter one last favourite dish:")
##fooddic[4]=food4
##print(fooddic)
##
##dislike=input("Enter the that you doesn't like :")
##key_to_remove=None
##for key,value in fooddic.items():
##    if value == dislike:
##        key_to_remove=key
##        break
##if key_to_remove:
##    del fooddic[key_to_remove]
##else:
##    print("It's not in your favourite!!")
##print(sorted(fooddic.values()))


##
##Enter a list of ten colours.
##Ask the user for a starting
##number between 0 and 4
##and an end number
##between 5 and 9. Display
##the list for those colours
##between the start and end
##numbers the user input.



##colour=["Blue","Green","Black","White","Brown","Red","Purple","Yellow","Orange"]
##ask=int(input("Enter a starting number between 0 and 4: "))
##ask2=int(input("Enter a Ending number between 5 and 9:"))
##print(colour[ask:ask2])



##Create a list of four three-digit
##numbers. Display the list to the
##user, showing each item from
##the list on a separate line. Ask
##the user to enter a three-digit
##number. If the number they
##have typed in matches one in
##the list, display the position of
##that number in the list,
##otherwise display the message
##“That is not in the list”.

##num=[234,678,675,865]
##for i in num:
##    print(i)
##userNum=int(input("Enter a three-digit number:"))
##if userNum in num:
##    print(f"Index of {userNum} is ", num.index(userNum))
##else:
##    print("choose from the above..")

##num=[234,678,675,865]
##for i in num:
##    print(i)
##userNum=int(input("Enter a three-digit number:"))
##if userNum in num:
##    print(f"Index of {userNum} is ", num.index(userNum))
##else:
##    print("choose from the above..")
    
##Ask the user to enter the names of three people they want to
##invite to a party and store them in a list. After they have entered
##all three names, ask them if they want to add another. If they do,
##allow them to add more names until they answer “no”. When
##they answer “no”, display how many people they have invited to
##the party

##count = 0
##people=[]
##for _ in range(3):
##    name=input("Enter the names you want to invite:")
##    people.append(name)
##    count +=1
##
##while True:
##    ask=input("Do you want to add more inviters:")
##    if ask == "yes":
##        name2=input("Enter the names you want to invite:")
##        people.append(name2)
##        count += 1
##        
##    else:
##        break
##print(people,count)
        
        
##Change program 076 so that once the user has completed their list of names, display the
##full list and ask them to type in one of the names on the list. Display the position of that
##name in the list. Ask the user if they still want that person to come to the party. If they
##answer “no”, delete that entry from the list and display the list again.


##count = 0
##people=[]
##for _ in range(3):
##    name=input("Enter the names you want to invite:")
##    people.append(name)
##    count +=1
##
##while True:
##    ask=input("Do you want to add more inviters:")
##    if ask == "yes":
##        name2=input("Enter the names you want to invite:")
##        people.append(name2)
##        count += 1
##        
##    else:
##        break
##print(people,count)
##ask2=input("Enter the one of the name from above list:")
##print(people.index(ask2))
##ask3=input(f"Do you still want {ask2} in your party:")
##if ask3 == "no":
##    people.remove(ask2)
##    print(people)
##else:
##    print("The name is not in the list..")
##print(len(people))
        

##Create a list containing the titles of
##four TV programmes and display
##them on separate lines. Ask the
##user to enter another show and a
##position they want it inserted into
##the list. Display the list again,
##showing all five TV programmes in
##their new positions.



##TvShows=["cooku with komali","bigg boss","vanakam Thamizha","Naanga vera maari"]
##for _ in TvShows:
##    print(_)
##ask1=TvShows.insert(2,input("Enter another show:"))
##print(TvShows)



##Create an empty list called “nums”.
##Ask the user to enter numbers.
##After each number is entered, add
##it to the end of the nums list and
##display the list. Once they have
##entered three numbers, ask them if
##they still want the last number they
##entered saved. If they say “no”,
##remove the last item from the list.
##Display the list of numbers.


##nums=[]
##for _ in range(3):
##    ask1=nums.append(input("Enter a number:"))
##print(nums)
##ask2=input("Do you still wants the last number(yes/no):")
##if ask2 == "no":
##    nums.pop(-1)
##    print(nums)
##else:
##    print(nums)
    



































































































