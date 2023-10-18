import pandas as pd
import math

visitedcities = []

data = pd.read_csv("coverteddata.csv")

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
                                    
def _route_finder():
    currentcity = 0
    distance = 0
    visitedcities.append(currentcity)
    while len(visitedcities) < len(data.index):
        currentcity, distance = _find_closest_path(currentcity, distance)
    visitedcities.append(0)
    print(distance)
    print(visitedcities)

def _is_prime_(Number):
    factoramount = 0
    for i in range(1, Number+1):
        if Number%i == 0:
            factoramount += 1
            if factoramount > 2:
                break
    if factoramount == 2 or Number == 1:
        return True
    else:
        return False

def main():
    _route_finder()

main()

