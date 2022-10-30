#Header 1- name assignmentNumber ProgramNumber Description
print("Welcome")
print("Program and Program Number")
print("Description")
print("------------------------")
#Loop if int is not "quit"
num = ""
while num != "quit":
    print("Enter quit to continue to next program.")
    #Ask for int
    num = input("Enter a number: ")
    #Check if negative, zero, or positive
    if num == "quit":
        state = "quit"
    elif int(num) > 0:
        state = "positive"
    elif int(num) == 0:
        state = "zero"
    elif int(num) < 0:
        state = "negative"
    #Tell of negative, zero, or positive
    print("Your input is " + state + ".")

#Header 2- name assignmentNumber ProgramNumber Description
#Loop if ammount is not quit
#Ask for ammount
#check if over 10,000
    #Tell if over 10,000
    #Loop again if yes
#divide by 20
#round down to nearest factor
#subtract the 20s from total value
#divide by 10
#round to nearest factor
#subtract the 10s from total value
#repeat for 5s and 1s, coins

#Header 3- name assignmentNumber ProgramNumber Description
#Loop if string is not quit
#Ask for string
#check if string is only letters
#check if string is only uppercase
#check if string is only lowercase
#check if string is only digits
#check if string is alphanumeric
#check if string starts with a capital
#check if string ends with a period

#Header 4- name assignmentNumber ProgramNumber Description
#Loop of income is not quit
#ask for income
#Check which bracket income is
#Determine % accordingly
#Calculate tax ammount using %
#Output tax ammount
