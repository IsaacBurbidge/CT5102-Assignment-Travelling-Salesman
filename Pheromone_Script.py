import pandas as pd
import os.path


pheromonegraph = []

#Initialises a Y x Y matrix
def _create_pheromone_matrix(pheromonegraphlength):
    for i in range(0,pheromonegraphlength):
        pheromoneList = []
        for j in range(0,pheromonegraphlength):
            if i != j:
                pheromoneList.append(100) # a base level of pheromones, equal across all paths 
            else:
                pheromoneList.append(-1) # null, aka. cant visit. 
        pheromonegraph.append(pheromoneList)

#Saves the pheromone graph as an external file
def _write_to_file():
    dataToWrite = pd.DataFrame(pheromonegraph)
    if os.path.isfile('./pheromones.csv'):
        os.remove('pheromones.csv')
    dataToWrite.to_csv('pheromones.csv', index = False)

#External function called to run this script
def _generate_pheromones(pheromonegraphlength):
    pheromones = pd.read_csv("pheromones.csv")
    if pheromones.shape[0] == pheromonegraphlength: # used to make sure the pheromone file stays the same size as the distance matrix
        pass
    else:
        _create_pheromone_matrix(pheromonegraphlength)
        _write_to_file()

