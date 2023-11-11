import pandas as pd
import math

visitedcities = []



def _find_closest_path(currentcity, distance):
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
    if(i == len(data.index)):
        distance += currentcitydistancedict[0]
    else:
        distance += currentcitydistancedict[i]
    visitedcities.append(nextcity)
    currentcity = nextcity
    return currentcity, distance
                                    
def _route_finder(firstcity):
    data = pd.read_csv("coverteddata.csv")
    currentcity = firstcity
    distance = 0
    visitedcities.append(currentcity)
    while len(visitedcities) < len(data.index):
        currentcity, distance = _find_closest_path(currentcity, distance)
    visitedcities.append(0)
    print(distance)
    print(visitedcities)


