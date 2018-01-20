__author__ = 'Michael Johansen'

import random
import string

class DNA:
    genes = []
    fitness = 0.0

    def __init__(self, num):
        self.genes = [0] * num
        for i in range(0, len(self.genes)):
            self.genes[i] = random.choice(string.ascii_letters)

    def getFitness(self):
        return self.fitness

    #calculate the likeness compared tot hte target string
    def calcFitness(self, target):
        fit = 0
        for i in range(0, len(self.genes)):
            if (self.genes[i]==target[i]):
                fit+=1
        self.fitness = fit/len(target)

    #return the phrase from the DNA of this word
    def getPhrase(self):
        return ''.join(self.genes)

    #combine the phrase of this DNA with another DNA
    def reproduce(self, mate):
        child = DNA(len(mate.genes))
        separation = random.randint(0,len(mate.genes))
        for i in range(0, len(self.genes)):
            if(i<separation):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = mate.genes[i]
        return child

    #randomly generate new values for this DNA's phrase
    def mutate(self, chance):
        for i in range(0, len(self.genes)):
            rand = random.uniform(0,1)
            if(rand<chance):
                self.genes[i] = random.choice(string.ascii_letters)
