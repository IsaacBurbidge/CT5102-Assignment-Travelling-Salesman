import pandas as pd
import math

visitedcities = []

#Finds the nearest city to the current city
def _find_closest_path(currentcity, distance):
    global data
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

#External function called to run this script                                    
def _route_finder(firstcity):
    global data
    data = pd.read_csv("converteddata.csv") # read the data
    currentcity = firstcity # 
    distance = 0
    visitedcities.append(currentcity)
    while len(visitedcities) < len(data.index):
        currentcity, distance = _find_closest_path(currentcity, distance)
    visitedcities.append(0)
    print(distance)
    print(visitedcities)


