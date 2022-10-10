#HEADER
print("Welcome")
print("Program and Program Number")
print("Description")
print("------------------------")

#Get user input for number 1
num1 = input('Please enter a number: ')
#Get user input for number 2
num2 = input('Please enter a number: ')
#Get user input for number 3
num3 = input('Please enter a number: ')
#Get user input for number 4
num4 = input('Please enter a number: ')
#Get user input for number 5
num5 = input('Please enter a number: ')

#Output number 1
print("{:.2f}".format(float(num1)))
#Output number 2
print("{:.2f}".format(float(num2)))
#Output number 3
print("{:.2f}".format(float(num3)))
#Output number 4
print("{:.2f}".format(float(num4)))
#Output number 5
print("{:.2f}".format(float(num5)))
#Add numbers together
sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)
#Output the result of numbers added together
print("{:.2f}".format(float(sum)))
#Average the numbers 
average = float(sum) / 5 
#Output the result of average of numbers
print("{:.2f}".format(float(average)))



