import random

def testNumber(number):
    primenumber = True

    for i in range(2, number-1):
        if number % i == 0:
            primenumber = False

    if number < 2:
        primenumber = False
    
    return primenumber

def getPrimenumbers(end, start = 2): #0 and 1 aren't primenumbers, primebumbers can't be negative
    
    primenumbers = []
    for i in range(end - start + 1):
        isPrimenumber = testNumber(i + start)
        if isPrimenumber:
            primenumbers.append(i + start)
    
    return primenumbers

def getPrimenumberstate(end, start = 2): #0 and 1 aren't primenumbers, primebumbers can't be negative
    primenumbers = {}
    for i in range(end - start + 1):
        isPrimenumber = testNumber(i + start)
        primenumbers[i + start] = isPrimenumber
    
    return primenumbers

def getRandomPrimenumber(end = 1024, start = 2):
    primenumbers = getPrimenumbers(end, start)
    if primenumbers == []:
        raise BaseException(f"getRandomPrimenumbers(end = {end}, start = {start}) >>> No Primenumbers Found!")
    else:
        randPrime = random.choice(primenumbers)
        return randPrime
