##twoDlist=[[1,2,3],[4,5,6],[7,8,9]]
##twoDlist[2][1]=0
##print(twoDlist)

##
##Create the following using a
##simple 2D list using the
##standard Python indexing:
##    


##Using the 2D list from program 096, ask the user to
##select a row and a column and display that value.

##twoDlist=[[1,2,3],[4,5,6],[7,8,9]]
##print(twoDlist)
##row,col=list(map(int,input("Select the row and column:").split()))
##num=twoDlist[row][col]
##print(num)



##Using the 2D list from program 096, ask the user
##which row they would like displayed and display
##just that row. Ask them to enter a new value and
##add it to the end of the row and display the row
##again.

##t2list=[[1,2,3],[4,5,6],[7,8,9]]
##print(t2list)
##ans=int(input("Enter a row you want:"))
##row=t2list[ans]
##print(row)
##
##ask=int(input("Enter a new value to add it in end:"))
##row.append(ask)
##print(row)



##Change your previous program
##to ask the user which row they
##want displayed. Display that
##row. Ask which column in that
##row they want displayed and
##display the value that is held
##there. Ask the user if they want
##to change the value. If they do,
##ask for a new value and change
##the data. Finally, display the
##whole row again.


##t2list=[[1,2,3],[4,5,6],[7,8,9]]
##
##num=int(input("which row do you want to display(0,1,2):"))
##row=t2list[num]
##print(row)
##
##num2=int(input("Which column do you want to display:"))
##col=row[num2]
##print(col)
####print(row[col])
##
##qstion=input("Do you want to change the value:").lower()
##if qstion == "yes":
##    nvalue=int(input("Enter your new value:"))
####    col2=row.index(col)
##    t2list[num][num2]=nvalue
##    print(t2list)
##else:
##    print("ok,that's fine...")
    







































