#header

num = int(input("Enter an integer less than 500: "))
divideInto = int(input("Enter an integer to divide it by: "))
i = divideInto
while i <= num:
    if i % divideInto == 0:
        print(str(i))
    i += 1
print("--------------")
#HEADER


lowerLimit = int(input("Enter a number: "))
upperLimit = int(input("Enter a higher number: "))
countOfNums = 0
sumOfNums = 0
i = lowerLimit + 1
while i < upperLimit:
    print(str(i))
    countOfNums += 1
    sumOfNums += i
    i += 1
print("Total Numbers Between: " + str(countOfNums))
print("Sum of Numbers Between: " + str(sumOfNums))
print("--------------")
countOfNums = 0
sumOfNums = 0
for i in range(lowerLimit, upperLimit):
    print(str(i))
    countOfNums += 1
    sumOfNums += i
print("Total Numbers Between: " + str(countOfNums))
print("Sum of Numbers Between: " + str(sumOfNums))


print("--------------")
#HEADER


text = input("Enter text: ")
for i in text:
    if i.isalpha() == True:
        print(i)
        print(i.swapcase())
    elif i.isdigit() == True:
        print("The original is " + i)
        print(i + " squared is " + str(int(i) ** 2))
    elif i == " ":
        print("SPACE")
    else:
        print(i + " is a special character.")


print("--------------")
#HEADER

newNumber = ""
numberList = []
while newNumber != "done":
    newNumber = input("Enter a floating point number: ")
    if newNumber == "done":
        continue
    numberList.append(float(newNumber))
    print("Enter 'done' once you have finished adding numbers.")

sumOfNums = 0
count = len(numberList)
for num in numberList:
    sumOfNums += num
print("Count of numbers entered: " + str(count))
print("Sum of numbers entered: " + str(sumOfNums))
print("Average of numbers entered: " + str(sumOfNums / count))