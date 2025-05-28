##from array import *
##nums=array=('i',[45,64,35,345,345])
##print(nums)       


##from array import *
##array=('i',[34,98,43,54,676,67,65555])
##more=int(input("Enter a number that you want to add:"))
##append=array.append(more)
##print(f"{more} is appended:{append}")
##pop=array.pop(-1)
##print(f"I popped the last number:{pop}")



##Ask the user for a list of five
##integers. Store them in an array.
##Sort the list and display it in
##reverse order.



##from array import *
##nums=array('i',[])
##for i in range(0,5):
##    num=int(input("Enter a integers:"))
##    nums.append(num)
##sorted_num=sorted(nums)
##reverse_num=sorted(nums,reverse=True)
##print(sorted_num,reverse_num)
####print(num.reverse())

##
##Create an array which will store a list of integers.
##Generate five random numbers and store them in
##the array. Display the array (showing each item on
##a separate line).




##from array import *
##import random
##nums=array('i',[])
##for i in range(0,5):
##    num=random.randint(1,1000)
##    nums.append(num)
##for i in nums:
##    print(i)
    
    


##Ask the user to enter numbers. If they enter a
##number between 10 and 20, save it in the array,
##otherwise display the message “Outside the
##range”. Once five numbers have been
##successfully added, display the message “Thank
##you” and display the array with each item shown
##on a separate line.



##from array import *
##nums=array('i',[])
##while len(nums)<5: 
##    num=int(input("Enter a number between 10 and 20:"))
##    if num>=10 and num<=20:
##        nums.append(num)
##    else:
##        print("Outside the range...")
##print("Thanking you")
##for i in nums:
##    print(i)



##Create an array which contains
##five numbers (two of which
##should be repeated). Display
##the whole array to the user. Ask
##the user to enter one of the
##numbers from the array and
##then display a message saying
##how many times that number
##appears in the list.




##from array import *
##nums=array('i',[23,23,23,56,56,12,14,13])
##print(*nums)
##ask=int(input("Enter a number from the array :"))
##count=0
##for i in nums:
##    if ask==i:
##        count+=1
##print(f"{ask} contains {count} times in the array.")
        

##Create two arrays (one
##containing three numbers that
##the user enters and one
##containing a set of five random
##numbers). Join these two arrays
##together into one large array.
##Sort this large array and display
##it so that each number appears
##on a separate line.

##from array import *
##import random
##
##arr1=array('i',[])
##arr2=array('i',[])
##newarr=array('i',[])
##
##for i in range(3):
##    usrEnter=int(input("Enter a number:"))
##    arr1.append(usrEnter)
##
##for j in range(5):
##    randomNum=random.randint(1,100)
##    arr2.append(randomNum)
##
##for num in arr1:
##    newarr.append(num)
##for num in arr2:
##    newarr.append(num)
##sortedarr=sorted(newarr)
##for k in sortedarr:
##    print(k)






##
##093
##Ask the user to enter five
##numbers. Sort them into order
##and present them to the user.
##Ask them to select one of the
##numbers. Remove it from the
##original array and save it in a
##new array.



##from array import array
##nums=array('i',[])
##delnum=array('i',[])
##for i in range(5):
##    num=int(input("Enter a five numbers:"))
##    nums.append(num)
##print(*nums)
##ask=int(input("select one of the number from the above:"))
##delnum.append(ask)
##nums.remove(ask)
##print(*delnum)





##Display an array of five
##numbers. Ask the user to
##select one of the numbers.
##Once they have selected a
##number, display the
##position of that item in the
##array. If they enter
##something that is not in
##the array, ask them to try
##again until they select a
##relevant item.




##from array import array
##import random
##nums=array('i',[])
##for i in range(5):
##    num=random.randint(1,100)
##    nums.append(num)
##print(*nums)
##usrchoice=int(input("Select a number from above:"))
##while usrchoice not in nums:
##    usrchoice=int(input("Try again..."))
##print(nums.index(usrchoice))



##Create an array of five numbers
##between 10 and 100 which each have
##two decimal places. Ask the user to
##enter a whole number between 2 and 5.
##If they enter something outside of that
##range, display a suitable error message
##and ask them to try again until they
##enter a valid amount. Divide each of the
##numbers in the array by the number the
##user entered and display the answers
##shown to two decimal places.            




##from array import array
##import random
##
##nums=array('i',[])
##ask1=array('i',[])
##divarr=array('f',[])
##
##for i in range(5):
##    num=random.randint(10,100)
##    nums.append(num)
##print("The generated numbers:",*nums)
##    
##ask1=int(input("Enter a number between 2 and 5:"))
##while  ask1 < 2 or ask1 > 5:
##    print("Go,Study the class UKG...")
##    ask1=int(input("Try again:"))
##
##for num in nums:
##    result=num/ask1
##    divarr.append(result)
##print(*divarr)
##    
























