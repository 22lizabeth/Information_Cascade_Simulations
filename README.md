# InformationCascadeSimulations
There are three sources of water available to the agents (Well 1, Well 2, and Well 3), but only one well actually has water each day and it may change day to day. Each agent may only choose to go to one source of water each day, and if they chose wrong, then they don't get water for the day. There are four simulations in the program that allow you to run this scenario and observe the affect of information cascades as well as the influence of trust in neighbors and prior probability beliefs.

**To run the program:**
Command line arguments: python main.py numAgents(int) numSimulation(1,2,3, and/or 4)
In the command line, type main.py and then type the number of agents you want as an int (1 - infinity) Then the simulation you would like to run as an int(1,2,3 or 4). You can run multiple simulations or just one. Each simulation run at the same time will have the same priors and trust for the agents for accurate comparison between simulations.

*In all simulations, agents make choices in sequential order so even if they 'have access' to all other agents information, they will really only be able to use the information from the agents that have chosen a well before them*

**Description of simulations:**
->Simulation One - Agents make choices based only on their own beliefs (priors)
->Simulation Two - Agents make choices based on their own beliefs modified by their neighbor's choices. This is a complete cycle network      and each agents has access to all of the other agents choices
->Simultation Three - Agents make choices the same as simulation two but with added utilities. These utilities can be modified to test how    they affect the agents decisions. They are currently set to (Well 1: 1, Well 2: 20, Well 3: 50)
->Simulation Four - Agents make choices the same as simulation two but in a specified order with a limited network. The current program       runs simulation four on a one cycle network and a two cycle network. The code is set up to be able to run it on as a high a cycle as you   want and can be modified easily to do so. There is an ad hoc network written into the code that can be run, but it can only be run on a     network of 10 agents so it is currently commented out.
