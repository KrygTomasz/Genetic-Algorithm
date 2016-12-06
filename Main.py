import numpy as numpy
#dane wejsciowe
numberOfPopulationMembers = 1000 #ilosc osobnikow w populacji
percentOfBestOnesToLive = .2 #20% najlepszych ma przezyc
probability = 0.000001 #prawdopodobienstwo


#algorytm genetyczny
def createNewPopulation(quantity, minimum, maximum):
    randomCoefficients = numpy.random.random(quantity)
    population = minimum+(randomCoefficients*(maximum-minimum))
    return population

def getBestMembers(populationX, populationY, percent, function):
    functionValues = function(populationX, populationY)
    sortedIndexes = functionValues.argsort()
    amountOfBestValues = int(len(functionValues)*percent)
    bestPopulationX = populationX[sortedIndexes[:amountOfBestValues]]
    bestPopulationY = populationY[sortedIndexes[:amountOfBestValues]]
    return [bestPopulationX, bestPopulationY]

def mutate(population):
    minimalPopulation = numpy.min(population)
    population += minimalPopulation*(probability*numpy.random.normal(0, 0.0001, len(population)))
    return population

def crossover(population, numberOfPopulationMembers): #wariant krzyzowania: srednia arytmetyczna
    populationLength = len(population)
    newPopulation = numpy.zeros(numberOfPopulationMembers)
    for i in range(populationLength):
        newPopulation[i] = population[i]
    i = populationLength
    while i < numberOfPopulationMembers:
        randomMemberIndex = numpy.random.randint(0, populationLength-1)
        firstRandomMember = population[randomMemberIndex]
        randomMemberIndex = numpy.random.randint(0, populationLength-1)
        secondRandomMember = population[randomMemberIndex]
        averageMember = (firstRandomMember + secondRandomMember) / 2.0
        newPopulation[i] = averageMember
        i += 1
    return newPopulation

#testowa funkcja jednej zmiennej:
def function(x,y):
    #funkcja Rosenbrocka: (1-x)*(1-x) + 100*(y-x*x)*(y-x*x)
    return x*x+y*y

#wywolanie algorytmu genetycznego:
leftSide = -100 #szukamy rozwiazania w przedziale <leftSide, rightSide>
rightSide = 100
populationX = createNewPopulation(numberOfPopulationMembers, leftSide, rightSide)
populationY = createNewPopulation(numberOfPopulationMembers, leftSide, rightSide)
i = 0
while i < 1000: #1000 iteracji
    tempPopulation = getBestMembers(populationX, populationY, percentOfBestOnesToLive, function)
    tempPopulationX = tempPopulation[0]
    tempPopulationY = tempPopulation[1]
    newPopulationX = crossover(tempPopulationX, numberOfPopulationMembers)
    newPopulationY = crossover(tempPopulationY, numberOfPopulationMembers)
    newPopulationX = mutate(newPopulationX)
    newPopulationY = mutate(newPopulationY)
    i += 1
    if i > 300:
        probability = 0.00000001





#wydrukowanie wyniku:
print numpy.min(function(newPopulationX, newPopulationY))