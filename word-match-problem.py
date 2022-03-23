import random
import string
import numpy as np

class DNA:
    def __init__(self, size, mutation_rate=0.1):
        self.mutation_rate = mutation_rate
        self.size = size
        self.phase = ''.join(random.choices(string.ascii_lowercase, k = self.size))
        self.fitness_score = 0

    def fitness(self, target):
        score = 0
        for i in range(self.size):
            if target[i] == self.phase[i]:
                score += 1
        self.fitness_score = score/self.size
        return self.fitness_score

    def crossover(self, parent_A, parent_B):
        half = int(self.size/2)
        self.phase  = parent_A[:half]
        self.phase += parent_B[half :]
    
    def mutation(self, target):
        phase = ''
        for i in range(self.size):
            if random.random() < self.mutation_rate:
                phase += random.choice(string.ascii_letters)
            else:
                phase += self.phase[i]
        
        self.phase = phase

        self.fitness(target)

    def getPhase(self):
        return self.phase

        
class Sample:
    def __init__(self, target, mutation_rate=0.1):
        self.samples = []
        self.size = len(target)
        self.target = target
        self.matingPool = []
        self.poolSize = 0
        self.gen = 0
        self.mutation_rate = mutation_rate

    def create_sample(self, size=1000):
        for i in range(size):
            self.samples.append(DNA(size = self.size, mutation_rate= self.mutation_rate))
    
    def evalutate(self):
        for sample in self.samples:
            sample.fitness(self.target)
        
    def createMatingPool(self):
        for sample in self.samples:
            for i in range(int(sample.fitness_score*100)):
               self.matingPool.append(sample)
        self.poolSize = len(self.matingPool)

    def reproduce(self):
        for i in range(self.size):
            parent_A = self.matingPool[np.random.randint(0, self.poolSize)]
            parent_B = self.matingPool[np.random.randint(0, self.poolSize)]
            self.samples[i].crossover(parent_A.getPhase(), parent_B.getPhase())
            self.samples[i].mutation(self.target)

    def evolution(self):
        while True:
            self.gen += 1
            population.evalutate()
            population.createMatingPool()
            population.reproduce()
            self.checkForSolution()

    def checkForSolution(self):
        for sample in self.samples:
            if sample.getPhase() == self.target:
                print("Reached Solution after ", self.gen," : ", self.target)



population = Sample(target='iamnoob', mutation_rate=0.2)
population.create_sample()
population.evolution()