import random as rand
import sys
from agent import *
from simulationHandler import *

def main():

    #In the command line run main.py and then type the number of agents you want as an int
    #Then the simulation you would like to run as an int(1,2,3 or 4).
    #You can run multiple simulations.
    #Simulation One - Agents make choices based only on their own beliefs (priors)
    #Simulation Two - Agents make choices based on their own beliefs modified by their neighbor's choices
    #Simultation Three - Agents make choices the same as sim two but with added utilities
    #Simulation Four - Agents make choices the same as sim two but in a specified order with a limited network

    #Select the correct water source for the day's simulations
    waterSource = rand.randint(1,3)
    print("Today\'s water source is well ", waterSource, "\n")

    #Create the list of agents with their priors and their likelihoods
    agentList = list()
    agentList = createAgents(int(sys.argv[1]),agentList,waterSource)

    #Create the simulation handler
    simHandler = SimulationHandler(agentList,waterSource)

    for i in range(2,len(sys.argv)):
        print("Running simulation: ",sys.argv[i])
        simHandler.runSimulation(int(sys.argv[i]))
        #Reset posteriors for further simulations
        for agent in agentList:
            agent.resetPosteriors()
        print("\n")

def createAgents(numAgents,agentList,waterSource):
    #print("Priors")
    for i in range(numAgents):
        #print("Agent", i+1, ":")

        #Generate random probabilities for priors for the agent
        probWellOne = round(rand.random(), 2)
        probWellTwo = round(rand.uniform(0,1-probWellOne),2)
        probWellThree = round((1 - (probWellOne + probWellTwo)),2)

        #Fix some prabilities to be correct or incorrect for experimentation
        #In this case, set first two agents to have correct information
        if (i == 0 or i == 1):
            if(waterSource == 1):
                probWellOne = .96
                probWellTwo = .02
                probWellThree = .02
            elif(waterSource == 2):
                probWellOne = .02
                probWellTwo = .96
                probWellThree = .02
            else:
                probWellOne = .02
                probWellTwo = .02
                probWellThree = .96

        #Print the prior probabilities
        #print(" Well 1:", probWellOne)
        #print(" Well 2:", probWellTwo)
        #print(" Well 3:", probWellThree)

        #Generate random trust in others probability for the agent
        trust = round(rand.random(), 2)
        if i == 4:
            trust = .61
        #print(" Trust: ", trust)

        #Create the agent and add it to the agent list
        agent = Agent(probWellOne,probWellTwo,probWellThree,trust)
        agentList.append(agent)
    #print("\n")

    return agentList

if __name__ == '__main__':
    main()
