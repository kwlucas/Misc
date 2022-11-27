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

def CountNegatives(paramOrigList):
    negativeCount = 0
    for i in paramOrigList:
        if i < 0:
            negativeCount += 1
    return negativeCount

def ReverseList(paramOrigList):
    reorderedList = []
    for i in paramOrigList:
        reorderedList.insert(0, i)
    return reorderedList

def GetListFirstLast(paramOrigList):
    newList = [paramOrigList.copy().pop(0), paramOrigList.copy().pop(-1)]
    return newList

def deleteNegatives(paramOrigList):
    listCopy = paramOrigList.copy()
    for i in listCopy:
        if i < 0:
            listCopy.remove(i)
    return listCopy

# -----------------------------------------------------------------------------------------------

print('PROGRAM 4 - Testing functions')
print('')
print('Testing program 2 function')
print('')
#ask user for string
userString = input('Please enter a string. ')
letterCount = CountChar(userString)
print('The string you entered has ' + str(letterCount) + ' character(s).')

print('')
print('Testing program 3 functions')
print('')
print('3a - new number list')
print('')

newList = GetNewNumberList()
print('The list returned by the function: ' + str(newList))
formattedList = ', '.join([str(i) for i in newList])
print('The values you entered, formatted nicely: ' + formattedList)

print('')
print('3b - Count the negative numbers')
print('')
newList = GetNewNumberList()
print('')
print('There are ' + str(CountNegatives(newList)) + ' negative numbers in the list.')
print('')

print('3c - Reverse list')
print()
newList = []
while True:
    userInput = input('Enter an item to put into the list. (or type "done" to finalize list.')
    if userInput != 'done':
        newList.append(userInput)
        continue
    break
    

print('')
print('The original list: ' + str(newList))
print('Reversed list: ' + str(ReverseList(newList)))
print('')

print('3d - First and last')
print()
newList = []
while True:
    userInput = input('Enter an item to put into the list. (or type "done" to finalize list.')
    if userInput != 'done':
        newList.append(userInput)
        continue
    break

print('First of list: ' + str(GetListFirstLast(newList)[0]))
print('Last of list: ' + str(GetListFirstLast(newList)[1]))

print()
print('3e - Delete negatives')
print()
newList = GetNewNumberList()
print('The original list: ' + str(newList))
print('The list without neagtives: ' + str(deleteNegatives(newList)))