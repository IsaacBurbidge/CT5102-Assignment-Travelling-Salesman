import pandas as pd

pheremonegraph = []

def _create_pheremone_matrix():
    for i in range(0,5000):
        pheremoneList = []
        for j in range(0,5000):
            if i != j:
                pheremoneList.append(100)
            else:
                pheremoneList.append(-1)
        pheremonegraph.append(pheremoneList)


def _write_to_file():
    dataToWrite = pd.DataFrame(pheremonegraph)
    dataToWrite.to_csv('pheremones.csv', index = False)



def _generate_pheremones():
    _create_pheremone_matrix()
    _write_to_file()
