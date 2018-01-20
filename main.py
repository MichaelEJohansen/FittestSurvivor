__author__ = 'Michael Johansen'

import tkinter as tk
import string
import DNA
import random
import time

maxPopSize = 200
target = ''
mutationChance = 0.005
genNumber = 0

population = []
matingPool = []

class genAlg(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        root.geometry('{}x{}'.format(400, 300))

        #Create an introduction, a prompt, in input box, and an output label
        self.prompt = tk.Label(self, text = "Write something short (No spaces, only letters):", anchor ="center")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text = "Submit", command = self.stringCalc)
        self.output = tk.Label(self, text = "")

        #Create the labels for the best, average, and worst cases, as well as an info button and box
        self.mid = tk.Label(self, text = "")
        self.last = tk.Label(self, text = "")
        self.genNum = tk.Label(self, text = "")
        self.infoButton = tk.Button(self, text = "What is this?", command = self.displayInfo)
        self.infoBox = tk.Label(self, text = "")

        #put the created buttons and bozes onto the window
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.mid.pack(side="top", fill="x", expand=True)
        self.last.pack(side="top", fill="x", expand=True)
        self.genNum.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="top", pady=10)
        self.infoButton.pack(side="top",fill="x")
        self.infoBox.pack(side="top",fill="x",pady=10)


    def stringCalc(self):
        #Initialize the Process
        target = self.entry.get()
        result = " "
        genNumber=0
        population.clear()
        #check for an empty entry
        if(target==""):
            self.output.configure(text="Please enter something")
            return
        if(not target.isalpha()):
            self.output.configure(text="Please enter only letters")
            return
        #initialize the first random population
        for i in range(0,maxPopSize):
            population.append(DNA.DNA(len(target)))

        while(result!=target):
            #initialize the mating process
            genNumber+=1
            matingPool.clear()
            time.sleep(.04)
            #create a weighted mating pool favoring the most 'fit'
            #by adding them to the list more than the least 'fit'
            for i in range(0, len(population)):
                population[i].calcFitness(target)
                mult = population[i].fitness * 100
                for j in range(0,int(mult)):
                    matingPool.append(population[i])

            sort = []
            #mate two random partners from the mating pool
            #which is to combine their string values
            for i in range(0,len(population)):
                father = matingPool[(random.randrange(0,len(matingPool)))]
                mother = matingPool[(random.randrange(0,len(matingPool)))]
                child = father.reproduce(mother)
                child.mutate(mutationChance)
                population[i] = child
                sort.append(population[i])
            #sort the list so that best, average, and worst can be displayed
            for i in range(0,len(population)):
                population[i].calcFitness(target)
            sort.sort(key=lambda DNA: DNA.fitness, reverse=True)
            result=sort[0].getPhrase()
            #update and display the valuies for best, average and worst case scenarios
            self.output.configure(text="Best: " + sort[0].getPhrase())
            self.mid.configure(text="Average: " + sort[100].getPhrase())
            self.last.configure(text="Worst: " + sort[199].getPhrase())
            self.genNum.configure(text="Generation Number: " + str(genNumber))
            root.update_idletasks()

    #The display info button
    def displayInfo(self):
        if(self.infoBox.cget("text")==""):
            self.infoBox.configure(text="This is a genetic algorithm designed to\n"
                                    "'learn' the word that you type into the box\n\n"
                                    "'Best' is the most similar to your word in this generation\n"
                                    "'Average' is what the average word in this generation looks like\n"
                                    "'Worst' is the least like your word in this generation")
        else:
            self.infoBox.configure(text="")

if __name__ == "__main__":
    root = tk.Tk()
    genAlg(root).pack(fill="both", expand=True)
    root.mainloop()