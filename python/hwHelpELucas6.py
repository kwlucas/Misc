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

# salary = float(input('Enter your salary: '))
# bonusPercent = float(input('Enter your bonus percent in decimal form: '))
# print(findBonus(salary, bonusPercent))

employeeList = []
salaryList = []
bonusPercentList = []
bonusList = []
while(True):
    employeeId = input('Enter the employee ID (Or quit if you are done entering): ')
    if employeeId == "quit":
        break
    employeeList.append(employeeId)
    salary = float(input('Enter the employee salary: '))
    salaryList.append(salary)
    bonusPercent = float(input('Enter the employee bonus percent (in decimal form): '))
    bonusPercentList.append(bonusPercent)
    bonusList.append(findBonus(salary, bonusPercent))
empoyeeCount = 0
totalBonuses = 0.00
for i in employeeList:
    print('ID: ' + i)
    print('Salary: ' + str(salaryList[empoyeeCount]))
    print('Bonus Percent: ' + str(bonusPercentList[empoyeeCount]))
    print('Bonus Amount: ' + str(bonusList[empoyeeCount]))
    totalBonuses += bonusList[empoyeeCount]
    empoyeeCount += 1

print()
print('Number of employees: ' + str(empoyeeCount))
print('Total Bonus Amount: ' + str(totalBonuses))
print('Average Bonus Amount: ' + str(totalBonuses / empoyeeCount))