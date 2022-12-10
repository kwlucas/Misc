# Function to count the words in an array.

def countWords(paramString):
    array = paramString.split()
    return len(array)

userString = input('Enter a string')

wordCount = countWords(userString)
print(wordCount)

def findBonus(paramSalary, paramBonusPercent):
    bonus = paramSalary * paramBonusPercent
    return bonus

salary = float(input('Enter your salary: '))
bonusPercent = float(input('Enter your bonus percent in decimal form: '))
print(findBonus(salary, bonusPercent))