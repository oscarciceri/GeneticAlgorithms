import Genetic

if __name__ == '__main__':

	numberGenerations = 10000
	repeatChromosome = 10

	population = [[0,1,1,0], [1,1,0,0], [1,0,1,1], [0,0,0,1]]

	g = Genetic.Algorithm(population, numberGenerations, repeatChromosome)
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