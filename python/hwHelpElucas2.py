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
print("Welcome")
print("Program and Program Number")
print("Description")
print("------------------------")
#Loop if amount is not quit
amount = ""
while amount != "quit":
    print("Enter quit to continue to next program.")
    #Ask for amount
    amount = input("Enter a dollar ammount: $")
    #check if over 10,000
    if amount == "quit":
        print("Quitting program")
        continue
    elif float(amount) > 10000:
        #Tell if over 10,000
        print("Ammount cannot be over $10,000.")
        #Loop again if yes
        continue
    else:
        amount = round(float(amount), 2)
    #divide by 20 and round down to nearest int
    twenties = (amount // 20)
    #subtract the 20s from total value
    amount -= (twenties * 20)
    #divide by 10
    tens = (amount // 10)
    #subtract the 10s from total value
    amount -= (tens * 10)
    #repeat for 5s and 1s, coins
    fives = (amount // 5)
    amount -= (fives * 5)
    ones = amount // 1
    amount -= ones
    quarters = amount // 0.25
    amount -= quarters * 0.25
    dimes = amount // 0.10
    amount -= dimes * 0.10
    nickles = amount // 0.05
    amount -= nickles * 0.05
    pennies = amount // 0.01
    amount -= pennies * 0.01
    print("Change needed: ")
    print("$20 Bills - " + str(twenties))
    print("$10 Bills - " + str(tens))
    print("$5 Bills - " + str(fives))
    print("$1 Bills - " + str(ones))
    print("Quarters - " + str(quarters))
    print("Dimes - " + str(dimes))
    print("Nickles - " + str(nickles))
    print("Pennies - " + str(pennies))


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
