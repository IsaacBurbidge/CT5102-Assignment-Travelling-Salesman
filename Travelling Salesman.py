import pandas as pd
import math

visitedcities = []

distance = 0

data = pd.read_csv("coverteddata.csv")

visitedcities = []


def _find_closest_path(currentcity, distance):
    i = 0
    currentcitydistancedict = {}
    #print(data.loc[currentcity])
    for item in data.loc[currentcity]:
        print(data.at[currentcity, item])
        currentcitydistancedict[i] = data.at[currentcity, item]
        i += 1
    
    sorteddistancelist = sorted(currentcitydistancedict)
    print(currentcitydistancedict[0])
    nextcity = 0 
    i = 0
    while nextcity in visitedcities:
        nextcity = sorteddistancelist[i]
        i += 1
        if(i == len(data.index)):
            break
    if(i == len(data.index)):
        distance += currentcitydistancedict[0]#[0][1]
        nextcity = 0
    else:
        distance += currentcitydistancedict.get(i)
    visitedcities.append(nextcity)
    currentcity = nextcity
    print(currentcity)
    return currentcity
                                    

def _route_finder():
    currentcity = 0
    distance = 0
    while len(visitedcities) < len(data.index):
        currentcity = _find_closest_path(currentcity, distance)
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

