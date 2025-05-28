##Ask the user to enter their
##first name and then display
##the length of their first name.
##Then ask for their surname
##and display the length of
##their surname. Join their first
##name and surname together
##with a space between and
##display the result. Finally,
##display the length of their full
##name (including the space)


##Fname=input("Enter your first name:")
##print(len(Fname))
##Sname=input("Enter your surname:")
##print(len(Sname))
##Fullname=Fname+" "+Sname
##print(Fullname)
##print(len(Fullname))



##Ask the user to type in their favourite school subject.
##Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.



##sub=input("Tell me your fav subject:")
####for letter in sub:
####    print(letter,end="-")
##print("-".join(sub))



##Show the user a line of text from your favourite poem
##and ask for a starting and ending point. Display the
##characters between those two points.



##poem="Twinkle,Twinkle litter star ,how i wonder what you want "
##print(poem)
##print(len(poem))
##Spoint=int(input("Enter your starting point:"))
##Epoint=int(input("Enter your Ending point:"))
##print(poem[Spoint:Epoint])


##Ask the user to type in a word in upper case. If they
##type it in lower case, ask them to try again. Keep
##repeating this until they type in a message all in
##uppercase.


##Ucase=input("Enter a word in uppercase:" )
##while Ucase.islower():
##    Ucase=input("Try again,make it in uppercase :")
##print("yes,its uppercase")    


##Ask the user to type in their
##postcode. Display the first
##two letters in uppercase.


##pcode=input("Type your postcode:")
##start=pcode[0:2]
##end=pcode[2:]
####print(start.upper())
##print(start.upper()+end)



##ask the user to type in their name
##and then tell them how many vowels
##are in their name.

##name=input("Enter your name :").strip().lower()
##vowels=["a","e","i","o","u"]
##
##count =0
##vletter=[]
##
##for letter in name:
##    if letter in vowels:
##        vletter.append(letter)
##        count += 1
##print(vletter)
##print(f"No of vowels your name :{count}")
    



##name = input("Enter your name: ").strip().lower()
##vowels = ["a", "e", "i", "o", "u"]
##
##count = 0
##vletter = []
##
##for letter in name:
##    if letter in vowels:
##        vletter.append(letter)
##        count += 1
##
##print("Vowels in your name:", vletter)
##print(f"Number of vowels in your name: {count}")



##Ask the user to enter a new password. Ask
##them to enter it again. If the two passwords
##match, display “Thank you”. If the letters are
##correct but in the wrong case, display the
##message “They must be in the same case”,
##otherwise display the message “Incorrect”.





##password=input("Enter your password:")
##Repwd=input("Enter it again:")
##if password == Repwd :
##    print("Thanking you...")
##elif password.lower() == Repwd.lower():
##    print("They must be same case..")
##else:
##    print("Incorrect....")






##Ask the user to type in a word and then
##display it backwards on separate lines. For
##instance, if they type in “Hello” it should
##display


##word=input("Enter a word:")
##length=len(word)
##num=1
##for x in word:
##    position=length-num
##    letter=word[position]
##    print(letter)
##    num+=1


##Create an array which will store a list of integers.
##Generate five random numbers and store them in
##the array. Display the array (showing each item on
##a separate line).


##import random
##from array import *
##list1=array('i',[])
##for num in range(5):
##    num=random.randint(1,100)
##    list1.append(num)
##    print(num)





##Ask the user to enter numbers. If they enter a
##number between 10 and 20, save it in the array,
##otherwise display the message “Outside the
##range”. Once five numbers have been
##successfully added, display the message “Thank
##you” and display the array with each item shown
##on a separate line.


from array import *
nums=array('i',[])
count=0
while count<5:
    num=int(input("Enter a number:"))
    if num>=10 and num<=20:
        nums.append(num)
        count+=1
    else:
        print("Outside of the range...")
   

print(*nums)
print("Thank you..")
        
    
    






























