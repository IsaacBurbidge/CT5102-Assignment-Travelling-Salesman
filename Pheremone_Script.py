import pandas as pd

pheremonegraph = []

#Initialises a 5000x5000 matrix
def _create_pheremone_matrix(pheremonegraphlength):
    for i in range(0,pheremonegraphlength):
        pheremoneList = []
        for j in range(0,pheremonegraphlength):
            if i != j:
                pheremoneList.append(100) # a base level of pheremones, equal across all paths 
            else:
                pheremoneList.append(-1) # null, aka. cant visit. 
        pheremonegraph.append(pheremoneList)

#Saves the pheremone graph as an external file
def _write_to_file():
    dataToWrite = pd.DataFrame(pheremonegraph)
    dataToWrite.to_csv('pheremones.csv', index = False)

#External function called to run this script
def _generate_pheremones(pheremonegraphlength):
    _create_pheremone_matrix(pheremonegraphlength)
    _write_to_file()

