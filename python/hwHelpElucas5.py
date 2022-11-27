numberList = []
while len(numberList) < 10:
    # Ask user for number
    userNumber = input('Please enter a number: ')
    # Use input.isDigit() to confirm a number
    if not userNumber.isdigit():
        print('Input is not a valid integer.')
        continue
    userNum = int(userNumber)
    # If the number is not already in the list apend number to list
    #Use the in operator as includes
    if userNum in numberList:
        print('Number is already in list please enter another number.')
        continue
    numberList.append(userNum)
# When the list contains 10 entries output the list contents
print('Your list now has 10 numbers!')
print('Your list: ' + str(numberList))
# use sum(ARRAY) to get sum. (Add comments describing how to do this without sum function)
sumOfList = sum(numberList)
avgOfList = sumOfList / len(numberList)
# Also output the sum, and average of the list
print('Sum of numbers: ' + str(sumOfList))
print('Average of numbers: ' + str(avgOfList))

# -----------------------------------------------------------------------------------------------
def CountChar(paramString):
    count = 0
    for i in paramString:
        count += 1
    return count
#ask user for string
userString = input('Please enter a string. ')
letterCount = CountChar(userString)
print('The string you entered has ' + str(letterCount) + ' character(s).')
# -----------------------------------------------------------------------------------------------
def GetNewNumberList():
    newNumberList = []
    userInput = ''
    while userInput != 'done':
        userInput = input('Please enter a number. ')
        convertInput = userInput.replace('.', '')
        convertInput = convertInput.replace('-', '')
        if not convertInput.isdigit():
            print('Input is not a valid integer or float please enter another number.')
            continue
        newNumberList.append(float(userInput))
    return newNumberList

newList = GetNewNumberList()
print('The list returned by the function ' + str(newList))
formattedList = ', '.join([str(i) for i in newList])
print('The values you entered, formatted nicely: ' + formattedList)

def CountNegatives(paramOrigList):
    negativeCount = 0
    for i in paramOrigList:
        if i < 0:
            negativeCount += 1
    return negativeCount
print('There are ' + str(CountNegatives(newList)) + ' negative numbers in the list.')
# -----------------------------------------------------------------------------------------------
def ReverseList(paramOrigList):
    reorderedList = []
    for i in paramOrigList:
        reorderedList.insert(0, i)
    return reorderedList

print('Reversed list: ' + str(ReverseList(newList)))