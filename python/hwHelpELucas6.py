# Function to count the words in an array.

def countWords(paramString):
    array = paramString.split()
    return len(array)

userString = input('Enter a string')

wordCount = countWords(userString)
print(wordCount)