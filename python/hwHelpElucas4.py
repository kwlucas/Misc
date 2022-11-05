#define function that takes three floats
def sumOfThree(float1, float2, float3):
    total = float1 + float2 + float3
    return total

def avgOfThree(float1, float2, float3):
    total = sumOfThree(float1, float2, float3)
    avg = total / 3
    return avg

def bigOfThree(float1, float2, float3):
    if float1 > float2 and float1 > float3:
        big = float1
    elif float2 > float1 and float2 > float3:
        big = float2
    else:
        big = float3
    return big

num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
num3 = float(input('Enter another number: '))

print(sumOfThree(num1, num2, num3))
print(avgOfThree(num1, num2, num3))
print(bigOfThree(num1, num2, num3))

print()
print()

def findArea(width, height):
    area = width * height
    return area

#get user input
num1 = float(input('Enter the width: '))
num2 = float(input('Enter the height: '))
#Print results
print(findArea(num1, num2))

print()
