import queensGenetic
import random

 #   ____  _     _ _______ _______ __   _ _______       _____  _     _ ______ ______        _______
 # |   __| |     | |______ |______ | \  | |______      |_____] |     |  ____/  ____/ |      |______
 # |____\| |_____| |______ |______ |  \_| ______|      |       |_____| /_____ /_____ |_____ |______
  

if __name__ == '__main__':

	numberGenerations = 100000
	repeatChromosome = 100
	sizePopulation = 4
	nGens = 8
	maxAllele = 7
	minAllele = 0
	chromosome = []
	population = []
	maxFitness = 28

# ____ ___ ____ ____ ___    ___  ____ ___  _  _ _    ____ ___ _ ____ _  _ 
# [__   |  |__| |__/  |     |__] |  | |__] |  | |    |__|  |  | |  | |\ | 
# ___]  |  |  | |  \  |     |    |__| |    |__| |___ |  |  |  | |__| | \| 
    
	for j in range(sizePopulation):
		for i in range(nGens):
			chromosome.append(random.randrange(minAllele, maxAllele, 1))
		population.append(chromosome.copy())
		chromosome.clear()
	
	# # chromosome for testing
	# chromosome = [7, 5, 3, 1, 6, 4, 2, 0] 
	# population.append(chromosome.copy())

	g = queensGenetic.Algorithm(population, numberGenerations, repeatChromosome, maxFitness, maxAllele, minAllele, nGens)
	g.printPopulation()
	g.run()
	# g.findFitness()
	# g.sortFitnessPopulation()
	# g.findAptitude()
	# g.windowing()
	# g.expTrans()
	# g.linearNorm()
	# g.findPDF()
	# g.findCDF()
	# g.bestChromosome()
	# g.rouletteMethod()
	# g.selectionCh()
	# g.reproduction()
	# g.mutation()
	# g.newGenerationElitism()


