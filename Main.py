from GeneticAlgorithm import GeneticAlgorithm


def function(x, y):
    # funkcja Rosenbrocka: (1-x)*(1-x) + 100*(y-x*x)*(y-x*x)
    return (1-x)*(1-x) + 100*(y-x*x)*(y-x*x)

numberOfPopulationMembers = 1000
percentOfBestOnesToLive = 0.2
searchingSection = [-100, 100]

GA = GeneticAlgorithm(numberOfPopulationMembers, percentOfBestOnesToLive, searchingSection, function)

#wydrukowanie wyniku:
GA.searchMinimum(iterations=1000)