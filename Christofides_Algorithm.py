import pandas as pd
import math


visitedcities = []

data = pd.read_csv("coverteddata.csv")


def _find_nearest_path():
    NextPathWeights = []
    for currentcity in visitedcities:
        currentcitydistancedict = list(data.loc[currentcity])
        sorteddistancelist = sorted(currentcitydistancedict)
        nextcity = 0
        i = 0
        if sorteddistancelist[0] == -1:
            i = 1
        while nextcity in visitedcities:
            currentdistance = sorteddistancelist[i]
            nextcity = currentcitydistancedict.index(currentdistance)
            i += 1
            if(i == len(data.index)):
                break
        NextPathWeights.append([currentdistance, nextcity])
    NextPathWeights = sorted(NextPathWeights)
    visitedcities.append(NextPathWeights[0][1])


#Prims
def _create_min_spanning_tree(startpoint):
    visitedcities.append(startpoint)
    while len(visitedcities) < 5000:
        _find_nearest_path()
        print(len(visitedcities))
    print(visitedcities)
    
