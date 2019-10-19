import numpy as np
from agent import *

class SimulationHandler:
    def __init__(self, agentList, waterLocation):
        self.agents = agentList
        self.waterLocation = waterLocation
        self.neighborChoices = list()
        self.simulation = {1: self.simulationOne, 2: self.simulationTwo, 3: self.simulationThree, 4: self.simulationFour}
        #Alligators at the first well mean almost certain death, the second is far away, and the third is most convenient
        self.wellUtilities = (1,20,50)
        #Initialize adjacency matrix to zeroes
        self.adjacencyMatrix = np.zeros((len(self.agents),len(self.agents)))

    def runSimulation(self,simNum):
        self.simulation[simNum]()

    def simulationOne(self):
        #Agents make their choices off of only private knowledge
        numFoundWater = 0
        for i in range(len(self.agents)):
            choice = self.agents[i].getChoice()
            #print("Agent", i+1, "chose:", choice)
            if(choice == self.waterLocation):
                numFoundWater += 1
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents")

    def simulationTwo(self):
        #Agents make choices off of their knowledge as well as their knowledge of their neighbors choices
        #Agents only know the choices of the neighbors that have already gone to fetch water
        #They don't know if the agents found water or not and thus base their choices on their trust in others
        self.neighborChoices.clear()
        numFoundWater = 0
        #Loop through all agents
        for i in range(len(self.agents)):
            #print("Agent",i+1,":")
            #Loop through the choices that each previous neighbor has made
            for neighborChoice in range(len(self.neighborChoices)):
                #print("Updating posteriors:")
                self.agents[i].updatePosteriors(self.neighborChoices[neighborChoice])
            #Agent makes a choice based on updated posteriors
            agentChoice = self.agents[i].getChoice()
            self.neighborChoices.append(agentChoice)
            #print("Agent", i+1, "chose:", agentChoice)
            if(agentChoice == self.waterLocation):
                numFoundWater += 1
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents")


    def simulationThree(self):
        #Agents make choices similiar to simulation two but with added utilities
        self.neighborChoices.clear()
        numFoundWater = 0
        #Loop through all agents
        for i in range(len(self.agents)):
            #print("Agent",i+1,":")
            #Loop through the choices that each previous neighbor has made
            for neighborChoice in range(len(self.neighborChoices)):
                #print("Updating posteriors:")
                self.agents[i].updatePosteriors(self.neighborChoices[neighborChoice])
            #Utilities are factored in to final posteriors
            self.agents[i].addUtilities(self.wellUtilities)
            #Agent makes a choice based on updated posteriors
            agentChoice = self.agents[i].getChoice()
            self.neighborChoices.append(agentChoice)
            #print("Agent", i+1, "chose:", agentChoice)
            if(agentChoice == self.waterLocation):
                numFoundWater += 1
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents")

    def simulationFour(self):
        #Cycle 1 - in order (each person can receive info from the two adjacent to them)
        print("Cycle 1:")
        self.neighborChoices.clear()
        numFoundWater = 0
        self.buildAdjacencyMatrix(1)
        #Loop through all the agents
        for i in range(len(self.agents)):
            #print("Agent",i+1,":")
            #Loop through the choices that the previous neighbor has made
            for neighborChoice in range(len(self.neighborChoices)):
                #Only take into account choices from neighbors the agent is connected to
                if(self.adjacencyMatrix[i,neighborChoice] == 1):
                    #print("Updating posteriors:")
                    self.agents[i].updatePosteriors(self.neighborChoices[neighborChoice])
            #Agent makes a choice based on updated posteriors
            agentChoice = self.agents[i].getChoice()
            self.neighborChoices.append(agentChoice)
            #print("Agent", i+1, "chose:", agentChoice)
            if(agentChoice == self.waterLocation):
                numFoundWater += 1
            self.agents[i].resetPosteriors()
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents\n")

        #Cycle 2 - each person knows their adjacent neighbors and then their adjacent neighbors
        print("Cycle 2:")
        self.neighborChoices.clear()
        numFoundWater = 0
        self.buildAdjacencyMatrix(2)
        #Loop through all the agents
        for i in range(len(self.agents)):
            #print("Agent",i+1,":")
            #Loop through the choices that the previous neighbor has made
            for neighborChoice in range(len(self.neighborChoices)):
                #Only take into account choices from neighbors the agent is connected to
                if(self.adjacencyMatrix[i,neighborChoice] == 1):
                    #print("Updating posteriors")
                    self.agents[i].updatePosteriors(self.neighborChoices[neighborChoice])
            #Agent makes a choice based on updated posteriors
            agentChoice = self.agents[i].getChoice()
            self.neighborChoices.append(agentChoice)
            #print("Agent", i+1, "chose:", agentChoice)
            if(agentChoice == self.waterLocation):
                numFoundWater += 1
            self.agents[i].resetPosteriors()
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents\n")

        #Ad hoc
        '''print("Ad hoc correct info:")
        self.adjacencyMatrix = np.array([[0,1,1,1,1,1,0,0,0,0],
                                        [1,0,1,0,0,0,1,0,0,0],
                                        [1,1,0,1,0,0,0,0,0,0],
                                        [1,0,1,0,1,0,0,0,0,0],
                                        [1,0,0,1,0,1,0,0,0,0],
                                        [1,0,0,0,1,0,1,0,0,0],
                                        [0,1,0,0,0,1,0,0,0,0],
                                        [0,0,0,0,0,0,1,0,1,1],
                                        [0,0,0,0,0,0,0,1,0,1],
                                        [0,0,0,0,0,0,0,1,1,0]])

        self.neighborChoices.clear()
        numFoundWater = 0
        #Loop through all the agents
        for i in range(len(self.agents)):
            print("Agent",i+1,":")
            #Loop through the choices that the previous neighbor has made
            for neighborChoice in range(len(self.neighborChoices)):
                #Only take into account choices from neighbors the agent is connected to
                if(self.adjacencyMatrix[i,neighborChoice] == 1):
                    print("Updating posteriors:")
                    self.agents[i].updatePosteriors(self.neighborChoices[neighborChoice])
            #Agent makes a choice based on updated posteriors
            agentChoice = self.agents[i].getChoice()
            self.neighborChoices.append(agentChoice)
            print("Agent", i+1, "chose:", agentChoice)
            if(agentChoice == self.waterLocation):
                numFoundWater += 1
            self.agents[i].resetPosteriors()
        print(numFoundWater, "agents found water out of", len(self.agents), "total agents\n")'''


    def buildAdjacencyMatrix(self, cycleNum):
        #Create an adjacency matrix for the agents based on the cycle
        self.adjacencyMatrix = np.zeros((len(self.agents),len(self.agents)))
        for agent in range(len(self.agents)):
            for neighbor in range(len(self.agents)):
                if abs(agent - neighbor) <= cycleNum and abs(agent - neighbor) != 0:
                    self.adjacencyMatrix[agent,neighbor] = 1
