class Agent:
    def __init__(self,probWellOne, probWellTwo, probWellThree, trust):
        self.priors = (probWellOne, probWellTwo, probWellThree)
        self.trustInOthers = trust
        self.posteriors = self.priors

    def getChoice(self):
        #Return the well number corresponding to the highest posterior probability
        for i in range(3):
            if max(self.posteriors) == self.posteriors[i]:
                return i+1

    def addUtilities(self,wellUtilities):
        #Update posteriors with well utilites
        probWellOne = wellUtilities[0] * self.posteriors[0]
        probWellTwo = wellUtilities[1] * self.posteriors[1]
        probWellThree = wellUtilities[2] * self.posteriors[2]
        self.posteriors = (probWellOne,probWellTwo,probWellThree)

        #print("After adding utilities:")
        #print(" Well 1:",self.posteriors[0])
        #print(" Well 2:",self.posteriors[1])
        #print(" Well 3:",self.posteriors[2])

    def updatePosteriors(self,neighborChoice):
        #Use Bayes Rule to re-calculate posterior probabilities, factoring in a neighbor's well choice
        #Get the likelihood probablities
        if(neighborChoice == 1):
            probChoiceGivenOne = self.trustInOthers
            probChoiceGivenTwo = (1 - self.trustInOthers) / 2
            probChoiceGivenThree = (1 - self.trustInOthers) / 2
        elif(neighborChoice == 2):
            probChoiceGivenTwo = self.trustInOthers
            probChoiceGivenOne = (1 - self.trustInOthers) / 2
            probChoiceGivenThree = (1 - self.trustInOthers) / 2
        else:
            probChoiceGivenThree = self.trustInOthers
            probChoiceGivenOne = (1 - self.trustInOthers) / 2
            probChoiceGivenTwo = (1 - self.trustInOthers) / 2
        #Get the probability that the neighbor would have made that well choice
        probChoice = (probChoiceGivenOne * self.posteriors[0]) + (probChoiceGivenTwo * self.posteriors[1]) + (probChoiceGivenThree * self.posteriors[2])

        if probChoice > 0:
            #Calculate and update posteriors factoring in neighbor's well choice
            #P(posteriors[0]|choice) - probOneGivenChoice
            probWellOne = round(((probChoiceGivenOne * self.posteriors[0]) / probChoice),2)
            #P(posteriors[1]|choice) - probTwoGivenChoice
            probWellTwo = round(((probChoiceGivenTwo * self.posteriors[1]) / probChoice),2)
            #P(posteriors[2|choice) - probThreeGivenChoice
            probWellThree = round(((probChoiceGivenThree * self.posteriors[2]) / probChoice),2)
            self.posteriors = (probWellOne,probWellTwo,probWellThree)

        #print("Well 1:",self.posteriors[0])
        #print("Well 2:",self.posteriors[1])
        #print("Well 3:",self.posteriors[2])

    def resetPosteriors(self):
        self.posteriors = self.priors

    def setPriors(self,newPriors):
        self.priors = newPriors
