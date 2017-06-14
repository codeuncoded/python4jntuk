#Exercise 2a
import math
x1 = int(raw_input("enter x1:"))
y1 = int(raw_input("enter y1:"))
x2 = int(raw_input("enter x2:"))
y2 = int(raw_input("enter y2:"))
distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
print distance

#Exercise 2b


#Exercise 3a

number = int(raw_input("enter a number"))
print "even" if number % 2 else "odd"

#3b
result = 0
for i in range(2, 11):
    result += 1/i
print result

#3c what is sequence

#3d
number = int(input("enter any number:"))
for i in range(number, -1, -1):
    print i

#4a
#some mistake
def isPrime(x):
    for i in range(2, x/2):
        if x % i:
            return False
    return True

primes = [x for x in range(5, 20000) if isPrime(x)]
print sum(primes) + 5

#5a

name = raw_input("enter a string:")

def countWordFrequency(name):
    wordFrequency = {}
    for char in name:
        if char in wordFrequency:
            wordFrequency[char] += 1
        else:
            wordFrequency[char] = 1
    return wordFrequency
print countWordFrequency(name)
#5b
#don't know what trace is

qoute = 'Do what you love. Postponing what you love doing is like saving up sex for old age -Warren Buffet'
words = qoute.split()
print words
date = '24/11/1987'
day, month, year = date.split('/')
print day, month, year
newDate = "/".join([day, month, year])
print newDate
#6a

#6a: not clear what 'these' lists mean
filename = 'sample.py'  #create a file named 'sample.py' on your local drive
file = open(filename, 'r')
fileContent = file.readlines()  #returns a list of strings: one string per line in the file
file.close()
fileContent = ''.join(fileContent)  #combining all lines to form one single string
print countWordFrequency(fileContent)

#7a
filename = 'sample.py'
file = open(filename, 'r')
fileContent = file.readlines()
fileContent.reverse()
for line in fileContent:
    print line

#7a other way
filename = 'sample.py'  #create a file named 'sample.py' on your local drive
file = open(filename, 'r')
fileContent = file.readlines()  #returns a list of strings: one string per line in the file
while fileContent:  #remember an empty list [] evaluates to False
    print fileContent.pop() #pop() removes the last element in the list

#7b


#8a

#8b

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def median(numbers):
    if not numbers:
        return 0
    sortedNumbers = sorted(numbers)
    length = len(sortedNumbers)
    return (sortedNumbers[length/2] + sortedNumbers[(length-1)/2])/2

#if you are going to sort numbers, there is simpler way to find mode
def mode(numbers):
    frequencies = countWordFrequency(numbers)
    maximum = None
    result = None
    for number, frequency in frequencies.items():
        if maximum < frequency:
            maximum = frequency
            result = number
    return result

numbers = [2,3,5,2,10,25]
print mean(numbers), median(numbers), mode(numbers)

#9a

def nearlyEqual(a,b):
    if len(a) != len(b):
        return False
    difference = False
    for chara, charb in zip(a, b):
        if chara != charb:
            if difference:
                return False
            else:
                difference = True
    return True

print nearlyEqual("sree", "srek")
print nearlyEqual("sree", "sek")
print nearlyEqual("sree", "serk")








