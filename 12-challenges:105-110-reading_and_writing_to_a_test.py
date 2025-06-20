##file=open("countries.txt","w")
##file.write("sweden\n")
##file.write("iceland\n")
##file.write("spain\n")
##file.close()
##file=open("countries.txt","r")
##print(file.read())
##file=open("countries.txt","a")
##file.write("Norway\n")
##file=open("countries.txt","r")
##print(file.read())




##Write a new file
##called
##“Numbers.txt”.
##Add five numbers
##to the document
##which are stored
##on the same line
##and only
##separated by a
##comma. Once you
##have run the
##program, look in
##the location where
##your program is
##stored and you
##should see that
##the file has been
##created. The
##easiest way to
##view the contents
##of the new text file
##on a Windows
##system is to read it
##using Notepad.



##file1=open("Numbers.txt","w")
##file1.write("1,2,3,4,5")
##file1=open("Numbers.txt","r")
##print(file1.read())


##Create a new file called “Names.txt”. Add five names to the
##document, which are stored on separate lines. Once you have
##run the program, look in the location where your program is
##stored and check that the file has been created properly.


##file=open("Names.txt","w")
##file.write("10nac\n")
##file.write("tenac\n")
##file.write("Mr.glitch\n")
##file.write("villagian\n")
##file=open("Names.txt","r")
##print(file.read())



##Open the Names.txt file. Ask the user to input a
##new name. Add this to the end of the file and
##display the entire file.


file=open("Names.txt","w")
usr_input=input("Enter your fav name:")
file=open("Names.txt","a")
file.write(usr_input)
file=open("Names.txt","r")
print(file.read())































































