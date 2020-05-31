import numpy as np
import threading
import random
import math


def fitnessFunction(chromosome, maxFitness):
	fitness = 0
	for i in range(len(chromosome)-1):
		for j in range(i+1,len(chromosome)):
			if ((chromosome[i]==chromosome[j]) or (chromosome[i]==chromosome[j]+j-i) or (chromosome[j]-j+i==chromosome[i])):
				fitness+=1

	fitness =  maxFitness - fitness
	return fitness

def sortFunction(fitness, population):
	idSortFitness = np.argsort(fitness)
	aux = population.copy()
	fitness.sort()
	j=0
	for i in idSortFitness:
		population[j]=aux[i]
		j=j+1

def aptitudeFunction(vector):
	aux = 0
	for i in range(len(vector)):
		vector[i] = vector[i] + aux 
		aux = vector[i]
	return vector

def windowingFunction(vector):
	minimum = min(vector)
	for i in range(len(vector)):
		vector[i] = vector[i]-minimum
	return vector

def expTransFunction(vector):
	minimum = min(vector)
	if minimum < 0:
		minimum = -1*minimum
	else:
		minimum = 0
	for i in range(len(vector)):
		vector[i] = math.sqrt(vector[i]+minimum+1)
	return vector

def linearNormFunction(vector):
	N = 10
	for i in range(len(vector)):
		vector[i] = i*N + 1
	return vector

def pdfFunction(vector):
	print(vector)
	suma = sum(vector)
	for i in range(len(vector)):
		vector[i] = vector[i]/suma
	return vector

def cdfFunction(pdf):
	aux = 0 
	for i in range(len(pdf)):
		pdf[i] = pdf[i] + aux
		aux = pdf[i]
	return pdf

def bestChFunction(population, pdf):
	index_max = np.argmax(pdf)
	bestCh = population[index_max]
	return bestCh

def rouletteFunction(population, cdf):
	randomValue = random.random()
	for i in range(len(cdf)):
		if(randomValue<cdf[i]):
			rouletteCh = population[i]
			break
	return rouletteCh

def crossoverFunction(parents,point):
	children = []
	c1 = []
	c2 = []
	p1 = parents[0]
	p2 = parents[1]
	for i in range(len(p1)):
		if i <= point:
			c1.append(p1[i])
			c2.append(p2[i])
		else:
			c1.append(p2[i])
			c2.append(p1[i])
	children.append(c1)
	children.append(c2)
	return children


def generativeFunction(vector, minAllele, maxAllele):
	newAllele = random.randrange(minAllele, maxAllele+1, 1)
	newLocus = random.randrange(0, len(vector), 1)
	vector[newLocus] = newAllele
	return vector
		
def swapFunction(vector):
	locus = random.randrange(0, len(vector), 1)
	return vector

def seqSwapFunction(vector, point):
	aux = []
	for i in range(len(vector)):
		if i <= point:
			aux.append(vector[i])
		else:
			aux.insert(0, vector[i])
	vector = aux
	return vector
			



class Algorithm:

	def __init__(self, population, numberGenerations, repeatChromosome,  maxFitness, maxAllele, minAllele, nGens):

		self.population = population
		self.populationSize = len(population)
		self.fitness = []
		self.aptitude = []
		self.pdf = []
		self.cdf = []
		self.bestCh = []
		self.rouletteCh = []
		self.parents = []
		self.children = []
		self.mutant = []
		self.numberGenerations = numberGenerations
		self.repeatChromosome = repeatChromosome
		self.maxFitness = maxFitness
		self.maxAllele = maxAllele
		self.minAllele = minAllele
		self.nGens = nGens


	def printPopulation(self):
		print("\nPopulation: ", self.population)

	def findFitness(self):
		for chromosome in self.population:
		 	value = fitnessFunction(chromosome.copy(), self.maxFitness)
		 	self.fitness.append(value)
		#print("Fitness: ", self.fitness)

	def sortFitnessPopulation(self):
		sortFunction(self.fitness, self.population)
		#print("Sort Fitness: ", self.fitness)
		#print("Sort Population: ", self.population)

	def findAptitude(self):
		self.aptitude = aptitudeFunction(self.fitness.copy())
		#print("Aptitude : ", self.aptitude)

	def windowing(self):
		self.aptitude = windowingFunction(self.fitness.copy())
		#print("Aptitude Windowing : ", self.aptitude )
	
	def expTrans(self):
		self.aptitude = expTransFunction(self.fitness.copy())
		#print("Aptitude Exponential Transformation : ", self.aptitude)

	def linearNorm(self):
		self.aptitude = linearNormFunction(self.fitness.copy())
		#print("Aptitude Linear Normalization : ", self.aptitude)

	def findPDF(self):
		self.aptitude  = linearNormFunction(self.fitness.copy())
		self.pdf = pdfFunction(self.aptitude.copy())
		#print("Probabilities PDF : ", self.pdf)

	def findCDF(self):
		self.cdf = cdfFunction(self.pdf.copy())
		#print("Probabilities CDF: ", self.cdf)

	def bestChromosome(self):
		self.bestCh = bestChFunction(self.population, self.pdf)
		print("Best Chromosome : ", self.bestCh, " with fitness = ", fitnessFunction(self.bestCh, self.maxFitness))

	def rouletteMethod(self):
		self.rouletteCh = rouletteFunction(self.population, self.cdf)
		#print("Chromosome Roulette: ", self.rouletteCh)

	def selectionCh(self):
		self.rouletteMethod()
		self.parents.append(self.rouletteCh.copy())
		self.parents.append(self.rouletteCh.copy())
		attempts = 0
		while self.parents[0] == self.parents[1]:
			self.rouletteMethod()
			self.parents[1]= self.rouletteCh.copy()
			attempts+=1
			if attempts==10:
				break
		#print("Selected Chromosomes: ", self.parents)


	def reproduction(self):
		#point = 3
		length = self.nGens
		point = random.randrange(0, length, 1)
		self.children = crossoverFunction(self.parents.copy(), point)
		#print("Children for reproduction: ", self.children)
		length = len(self.children)
		idCh = random.randrange(0, length, 1)
		self.children[idCh] = generativeFunction(self.children[idCh].copy(), self.minAllele, self.maxAllele)
		#self.children[selectChilden] = swapFunction(self.children[selectChilden].copy())



	def mutation(self):
		length = self.nGens
		point = random.randrange(0, length, 1)
		self.rouletteMethod()
		self.mutant = seqSwapFunction(self.rouletteCh.copy(), point)
		#print("Child for mutation with seqSwap: ", self.mutant)
		self.mutant = generativeFunction(self.mutant.copy(), self.minAllele, self.maxAllele)
		#print("Child for mutation with generative: ", self.mutant)


	def newGenerationElitism(self):
		aux = self.population
		self.population.clear()
		self.population.append(self.bestCh.copy())
		self.population.append(self.children[0].copy())
		self.population.append(self.children[1].copy())
		self.population.append(self.mutant.copy())
		print("New population: ", self.population)
		self.fitness.clear()
		self.aptitude.clear()
		self.pdf.clear()
		self.cdf.clear()
		self.bestCh.clear()
		self.rouletteCh.clear()
		self.parents.clear()
		self.children.clear()
		self.mutant.clear()

# ____ _  _ _  _ _  _ _ _  _ ____    ____ ____ 
# |__/ |  | |\ | |\ | | |\ | | __    | __ |__| 
# |  \ |__| | \| | \| | | \| |__]    |__] |  | 
	def run(self):
		print("Running GE")
		generation = 0
		nrepeat = 0
		running = True
		while running:
			print("Generation", generation)
			generation+=1

			self.findFitness()
			self.sortFitnessPopulation()
			self.findAptitude()
			self.findPDF()
			self.findCDF()
			self.bestChromosome()
			self.selectionCh()
			self.reproduction()
			self.mutation()
			self.newGenerationElitism()

# ____ ___ ____ ___  ___  _ _  _ ____    ____ ____ _ ___ ____ ____ _ ____ 
# [__   |  |  | |__] |__] | |\ | | __    |    |__/ |  |  |___ |__/ | |__| 
# ___]  |  |__| |    |    | | \| |__]    |___ |  \ |  |  |___ |  \ | |  | 
                                                                        
			if(generation > self.numberGenerations):
				running = False
			elif(fitnessFunction(self.population[0].copy(), self.maxFitness)==self.maxFitness):
				running = False
			elif(nrepeat > self.repeatChromosome):
				running = False
			else:
				running = True

		print("\n\n\n *************  ANSWER ************** \n\n") 
		print("\nGeneration = ", generation,
		      "\nBest Chromosome = ", self.population[0],
		      "\nFitness = ", fitnessFunction(self.population[0].copy(), self.maxFitness))
		





