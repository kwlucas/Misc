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
    print()

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
    print()


#Header 3- name assignmentNumber ProgramNumber Description
print("Welcome")
print("Program and Program Number")
print("Description")
print("------------------------")
#Loop if string is not quit
string = ""
while string != "quit":
    print("Enter quit to continue to next program")
    #Ask for string
    string = input("Enter text: ")
    #check if string is only letters
    if string.isalpha() == True:
        print("The string has only letters")
    #check if string is only uppercase
    if string.isupper() == True:
        print("The string is all uppercase")
    #check if string is only lowercase
    elif string.islower() == True:
        print("The string is all lowercase")
    #check if string is only digits
    if string.isdigit() == True:
        print("The string has only digits")
    #check if string is alphanumeric
    if string.isalnum() == True:
        print("The string is alpha-numeric.")
    #check if string starts with a capital
    if string[0].isupper() == True:
        print("The string starts with a capital letter.")
    #check if string ends with a period
    if string.endswith(".") == True:
        print("The string ends with a period.")
    print()

    #Header 4- name assignmentNumber ProgramNumber Description
print("Welcome")
print("Program and Program Number")
print("Description")
print("------------------------")
#Loop of income is not quit
income = ""
while income != "quit":
    print("Enter quit to exit program.")
    #ask for income
    income = input("Enter your income: $")
    if income == "quit":
        print("Exiting program.")
        continue
    else:
        income = round(float(income), 2)
    #Check which bracket income is and determine % accordingly
    if income <= 50000:
        tax = 0.01
    elif income <= 75000:
        tax = 0.02
    elif income <= 100000:
        tax = 0.03
    elif income <= 250000:
        tax = 0.04
    elif income <= 500000:
        tax = 0.05
    else:
        tax = 0.06
    #Calculate tax ammount using %
    taxAmount = income * tax
    #Output tax ammount
    print("The amount of income tax you owe is: $" + str(taxAmount))
    print()
