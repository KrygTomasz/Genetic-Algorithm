import numpy as numpy

class GeneticAlgorithm:

    def __init__(self, numberOfPopulationMembers, percentOfBestOnesToLive, section, function):
        self.numberOfPopulationMembers = numberOfPopulationMembers
        self.percentOfBestOnesToLive = percentOfBestOnesToLive
        self.section = section
        self.function = function
        self.populationX = []
        self.populationY = []

    def generateInitialPopulation(self):
        self.populationX = self.createNewPopulation()
        self.populationY = self.createNewPopulation()

    def createNewPopulation(self):
        minimum = self.section[0]
        maximum = self.section[1]
        randomCoefficients = numpy.random.random(self.numberOfPopulationMembers)
        population = minimum + (randomCoefficients * (maximum - minimum))
        return population

    def getBestMembers(self):
        functionValues = self.function(self.populationX, self.populationY)
        sortedIndexes = functionValues.argsort()
        amountOfBestValues = int(len(functionValues) * self.percentOfBestOnesToLive)
        bestPopulationX = self.populationX[sortedIndexes[:amountOfBestValues]]
        bestPopulationY = self.populationY[sortedIndexes[:amountOfBestValues]]
        return [bestPopulationX, bestPopulationY]

    def mutate(self):
        probability = 0.000001
        minimalPopulationX = numpy.min(self.populationX)
        minimalPopulationY = numpy.min(self.populationY)
        self.populationX += minimalPopulationX * (probability * numpy.random.normal(0, 0.0001, len(self.populationX)))
        self.populationY += minimalPopulationY * (probability * numpy.random.normal(0, 0.0001, len(self.populationY)))

    def crossover(self):
        populationXLength = len(self.populationX)
        populationYLength = len(self.populationY)
        newPopulationX = numpy.zeros(self.numberOfPopulationMembers)
        newPopulationY = numpy.zeros(self.numberOfPopulationMembers)
        for i in range(populationXLength):
            newPopulationX[i] = self.populationX[i]
            newPopulationY[i] = self.populationY[i]
        i = populationXLength
        while i < self.numberOfPopulationMembers:

            randomMemberIndexX = numpy.random.randint(0, populationXLength - 1)
            firstRandomMemberX = self.populationX[randomMemberIndexX]
            randomMemberIndexX = numpy.random.randint(0, populationXLength - 1)
            secondRandomMemberX = self.populationX[randomMemberIndexX]
            averageMemberX = (firstRandomMemberX + secondRandomMemberX) / 2.0

            newPopulationX[i] = averageMemberX

            randomMemberIndexY = numpy.random.randint(0, populationYLength - 1)
            firstRandomMemberY = self.populationY[randomMemberIndexY]
            randomMemberIndexY = numpy.random.randint(0, populationYLength - 1)
            secondRandomMemberY = self.populationY[randomMemberIndexY]
            averageMemberY = (firstRandomMemberY + secondRandomMemberY) / 2.0
            newPopulationY[i] = averageMemberY

            i += 1
        self.populationX = newPopulationX
        self.populationY = newPopulationY

    def searchMinimum(self, iterations):
        self.generateInitialPopulation()
        i = 0
        while i < iterations:  # 1000 iteracji
            tempPopulation = self.getBestMembers()
            self.populationX = tempPopulation[0]
            self.populationY = tempPopulation[1]
            self.crossover()
            self.mutate()
            i += 1
            if i > 300:
                probability = 0.00000001

        print numpy.min(self.function(self.populationX, self.populationY))